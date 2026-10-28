#!/usr/bin/env python3
"""Collect public pages into a private local cache; never import calendar events."""
from __future__ import annotations
import argparse, datetime as dt, email.utils, fcntl, hashlib, json, re, time, urllib.error, urllib.parse, urllib.request, urllib.robotparser
from html.parser import HTMLParser
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT/'.collector-cache'
CONFIG=ROOT/'data/collector-sources.json'
HISTORY=ROOT/'data/collection-runs.json'
UA='OpenWeekAmsterdamCollector/1.0'
MAX_BYTES=2_000_000
TZ=ZoneInfo('Europe/Amsterdam')

def read_json(path,default):
    if not path.exists(): return default
    return json.loads(path.read_text(encoding='utf-8'))

def write_json(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.tmp')
    tmp.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    tmp.replace(path)

def host_of(url):
    return (urllib.parse.urlsplit(url).hostname or '').lower().removeprefix('www.')

def clean(text): return re.sub(r'\s+',' ',text).strip()

class Anchors(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.items=[]; self.current=None
    def handle_starttag(self,tag,attrs):
        if tag=='a' and self.current is None:
            self.current={'href':dict(attrs).get('href',''),'text':[]}
    def handle_data(self,data):
        if self.current is not None:self.current['text'].append(data)
    def handle_endtag(self,tag):
        if tag=='a' and self.current is not None:
            self.items.append((self.current['href'],clean(' '.join(self.current['text'])))); self.current=None

class Articles(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.items=[];self.item=None;self.title=False;self.content=False;self.depth=0;self.skip=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);classes=a.get('class','').split()
        if tag=='article' and self.item is None:
            self.item={'title':'','url':'','publishedAt':None,'excerpt':''};self.depth=0
        if self.item is None:return
        if tag in ('h1','h2','h3') and 'entry-title' in classes:self.title=True
        if self.title and tag=='a':self.item['url']=a.get('href','')
        if tag=='time' and 'entry-date' in classes:self.item['publishedAt']=a.get('datetime')
        if tag=='div' and 'entry-content' in classes:self.content=True;self.depth=1
        elif self.content and tag=='div':self.depth+=1
        if self.content and tag in ('script','style'):self.skip+=1
    def handle_data(self,data):
        if self.item is None:return
        if self.title:self.item['title']+=' '+data
        if self.content and not self.skip:self.item['excerpt']+=' '+data
    def handle_endtag(self,tag):
        if self.item is None:return
        if tag in ('h1','h2','h3') and self.title:self.title=False
        if self.content and tag in ('script','style') and self.skip:self.skip-=1
        if self.content and tag=='div':
            self.depth-=1
            if not self.depth:self.content=False
        if tag=='article':
            self.item['title']=clean(self.item['title']);self.item['excerpt']=clean(self.item['excerpt'])[:1800]
            if self.item['title'] and self.item['url']:self.items.append(self.item)
            self.item=None;self.title=False;self.content=False;self.skip=0

def parse_station(html,url,start,end):
    parser=Anchors();parser.feed(html);groups={}
    for href,label in parser.items:
        dest=urllib.parse.urljoin(url,href);p=urllib.parse.urlsplit(dest)
        if p.scheme!='https' or host_of(dest)!=host_of(url):continue
        match=re.fullmatch(r'/platform/(?:msc|art)/[^/]+-(\d{4}-\d{2}-\d{2})/?',p.path)
        if not match:continue
        day=match.group(1)
        try:dt.date.fromisoformat(day)
        except ValueError:continue
        dest=urllib.parse.urlunsplit((p.scheme,p.netloc,p.path,'',''))
        row=groups.setdefault(dest,{'kind':'calendar_lead','url':dest,'date':day,'texts':[]})
        if label and label not in row['texts']:row['texts'].append(label)
    rows=[]
    for row in groups.values():
        texts=row.pop('texts');line=' | '.join(texts);tm=re.search(r'\b(\d{1,2}:\d{2})\s*[-–]\s*(\d{1,2}:\d{2})\b',line);money=re.search(r'€\s*(\d+[,.]\d{2})',line)
        row.update({'title':texts[0] if texts else '', 'calendarText':line[:1000], 'startTime':tm.group(1) if tm else None,'endTime':tm.group(2) if tm else None,'priceText':money.group(0) if money else None,'inWindow':start<=row['date']<=end,'needsReview':True})
        rows.append(row)
    return sorted(rows,key=lambda x:(x['date'],x['url']))

def parse_articles(html,url,start,end):
    parser=Articles();parser.feed(html);out=[];seen=set()
    for item in parser.items:
        dest=urllib.parse.urljoin(url,item['url']);parts=urllib.parse.urlsplit(dest)
        dest=urllib.parse.urlunsplit((parts.scheme,parts.netloc,parts.path,'',''))
        if parts.scheme!='https' or host_of(dest)!=host_of(url) or dest in seen:continue
        seen.add(dest);item.update({'kind':'article_lead','url':dest,'eventDate':None,'inWindow':None,'needsReview':True})
        out.append(item)
    return out

def parse_event_links(html,url,start,end,path_pattern):
    # Link discovery only: paths or publication dates are never event dates.
    parser=Anchors();parser.feed(html);found={}
    for href,label in parser.items:
        dest=urllib.parse.urljoin(url,href);parts=urllib.parse.urlsplit(dest)
        if parts.scheme!='https' or host_of(dest)!=host_of(url) or not re.fullmatch(path_pattern,parts.path) or len(label)<4:continue
        dest=urllib.parse.urlunsplit((parts.scheme,parts.netloc,parts.path,'',''))
        if dest not in found:
            found[dest]={'kind':'event_page_lead','url':dest,'title':label[:200],'eventDate':None,'inWindow':None,'needsReview':True}
    return list(found.values())

def parse_oba(html,url,start,end):
    return parse_event_links(html,url,start,end,r'/nl/agenda/(?!volledige-agenda/?$)[^/]+/?')
class PakhuisCards(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.row=None;self.depth=0;self.field=None;self.field_depth=0;self.items=[];self.skip=0
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);classes=a.get('class','').split()
        if tag=='div' and self.row is None and 'program' in classes and 'teaser' in classes:self.row={'title':'','url':'','scheduleText':''};self.depth=1;return
        if self.row is None:return
        if tag=='div':
            self.depth+=1
            if 'title' in classes and 'subtitle' not in classes:self.field='title';self.field_depth=self.depth
            elif 'date-time' in classes:self.field='scheduleText';self.field_depth=self.depth
        if tag=='a' and 'program-link' in classes:self.row['url']=a.get('href','')
        if tag in ('script','style'):self.skip+=1
    def handle_data(self,data):
        if self.row is not None and self.field and not self.skip:self.row[self.field]+=' '+data
    def handle_endtag(self,tag):
        if self.row is None:return
        if tag in ('script','style') and self.skip:self.skip-=1
        if tag=='div':
            if self.field and self.field_depth==self.depth:self.field=None
            self.depth-=1
            if self.depth==0:
                for k in ('title','scheduleText'):self.row[k]=clean(self.row[k])
                if self.row['title'] and self.row['url']:self.items.append(self.row)
                self.row=None

class WijkSlides(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True);self.row=None;self.depth=0;self.title=False;self.recurrence=False;self.script=False;self.items=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs);classes=a.get('class','').split()
        if tag=='div' and self.row is None and 'slide' in classes:self.row={'title':'','scheduleText':'','script':''};self.depth=1;return
        if self.row is None:return
        if tag=='div':self.depth+=1
        if tag=='h1':self.title=True
        if tag=='span' and 'event_recurrence' in classes:self.recurrence=True
        if tag=='script' and not a.get('src'):self.script=True
    def handle_data(self,data):
        if self.row is None:return
        if self.title:self.row['title']+=' '+data
        if self.recurrence:self.row['scheduleText']+=' '+data
        if self.script:self.row['script']+=data
    def handle_endtag(self,tag):
        if self.row is None:return
        if tag=='h1':self.title=False
        if tag=='span' and self.recurrence:self.recurrence=False
        if tag=='script':self.script=False
        if tag=='div':
            self.depth-=1
            if self.depth==0:
                self.row['title']=clean(self.row['title']);self.row['scheduleText']=clean(self.row['scheduleText'])
                self.items.append(self.row);self.row=None

def parse_pakhuis(html,url,start,end):
    parser=PakhuisCards();parser.feed(html);out=[];seen=set()
    for row in parser.items:
        dest=urllib.parse.urljoin(url,row['url']);parts=urllib.parse.urlsplit(dest)
        if parts.scheme!='https' or host_of(dest)!=host_of(url) or not re.fullmatch(r'/programma/[^/]+/?',parts.path):continue
        dest=urllib.parse.urlunsplit((parts.scheme,parts.netloc,parts.path,'',''))
        if dest in seen:continue
        seen.add(dest);out.append({'kind':'event_page_lead','url':dest,'title':row['title'],'scheduleText':row['scheduleText'],'eventDate':None,'inWindow':None,'needsReview':True})
    return out

def parse_wijkconnect(html,url,start,end):
    parser=WijkSlides();parser.feed(html);out=[];seen=set()
    pattern=r'https://www\.wijkconnect\.com/amsterdam/organisaties/8345/huis-van-de-buurt-de-boomsspijker/agenda/[0-9]+/[a-zA-Z0-9_-]+'
    for row in parser.items:
        match=re.search(pattern,row['script'])
        if not match or not row['title'] or match.group(0) in seen:continue
        dest=match.group(0);seen.add(dest);out.append({'kind':'activity_lead','url':dest,'title':row['title'],'scheduleText':row['scheduleText'],'eventDate':None,'inWindow':None,'needsReview':True})
    return out

ADAPTERS={'station_west_calendar':parse_station,'wordpress_articles':parse_articles,'oba_agenda_links':parse_oba,'pakhuis_agenda_links':parse_pakhuis,'wijkconnect_agenda_links':parse_wijkconnect}

CANDIDATE_KEYS=('kind','url','title','date','eventDate','startTime','endTime','priceText','inWindow','publishedAt','scheduleText','needsReview')
def valid_source(source):
    sid=source.get('id','');url=source.get('url','')
    if not isinstance(sid,str) or not isinstance(url,str):return False
    parts=urllib.parse.urlsplit(url);keys={k.lower() for k,_ in urllib.parse.parse_qsl(parts.query,keep_blank_values=True)}
    return bool(re.fullmatch(r'[a-z0-9][a-z0-9_-]*',sid) and parts.scheme=='https' and host_of(url) and not parts.username and not parts.password and not keys.intersection({'token','access_token','api_key','key','secret','password','session','auth','code'}) and source.get('adapter') in ADAPTERS)

def candidate_summaries(rows):return [{k:r[k] for k in CANDIDATE_KEYS if k in r} for r in rows]

def reparse(source,start,end,run_dir,original_run):
    sid=source.get('id','');url=source.get('url','');host=host_of(url)
    base={'sourceId':sid,'name':source.get('name',sid),'domain':host,'sourceUrl':url,'method':'deterministic-cache-reparse','startedAt':stamp(),'outcome':'cache_missing','httpStatus':None,'candidateCount':0,'datedInWindow':0,'undatedCandidates':0,'windowStart':start,'windowEnd':end,'cacheKey':None,'sha256':None,'message':''}
    if not valid_source(source):
        base.update(outcome='configuration_error',message='Source URL, identifier or adapter is invalid.');return base
    if not re.fullmatch(r'[0-9]{8}T[0-9]{12}Z',original_run):
        base.update(outcome='configuration_error',message='Invalid cache run id.');return base
    previous=read_json(CACHE/'runs'/original_run/'run.json',{})
    prior=next((x for x in previous.get('results',[]) if x.get('sourceId')==sid and x.get('cacheKey')),None)
    if not prior or prior.get('sourceUrl')!=url or source.get('adapter') not in ADAPTERS:
        base['message']='No matching cached HTML for this source and run.';return base
    rel=Path(prior['cacheKey'])
    try:
        file=(CACHE/rel).resolve();file.relative_to((CACHE/'runs').resolve());raw=file.read_bytes()
    except (ValueError,OSError):base['message']='Cached HTML is missing or outside the cache.';return base
    digest=hashlib.sha256(raw).hexdigest()
    if digest!=prior.get('sha256'):
        base.update(outcome='cache_integrity_error',message='Cached HTML does not match its recorded SHA-256.');return base
    base.update(cacheKey=prior['cacheKey'],sha256=digest,httpStatus=prior.get('httpStatus'),sourceFetchedAt=prior.get('sourceFetchedAt') or prior.get('startedAt'),snapshotRunId=original_run)
    try:
        rows=ADAPTERS[source['adapter']](raw.decode('utf-8','replace'),url,start,end)
        candidate_path=run_dir/(sid+'.candidates.json');write_json(candidate_path,rows)
        base.update(outcome='success' if rows else 'no_matches',candidateCount=len(rows),datedInWindow=sum(x.get('inWindow') is True for x in rows),undatedCandidates=sum(x.get('inWindow') is None for x in rows),candidates=candidate_summaries(rows),candidateCacheKey=str(candidate_path.relative_to(CACHE)),message='Reparsed cached HTML; no network request. Candidates need review and the snapshot may be stale.')
    except Exception as e:base.update(outcome='parser_error',message=f'{type(e).__name__}: {str(e)[:180]}')
    return base

class SameSiteRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):
        if urllib.parse.urlsplit(newurl).scheme!='https' or host_of(req.full_url)!=host_of(newurl):
            raise urllib.error.URLError('redirect outside source website')
        return super().redirect_request(req,fp,code,msg,headers,newurl)

OPENER=urllib.request.build_opener(SameSiteRedirect())
def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'text/html,text/plain;q=0.9,*/*;q=0.1'})
    with OPENER.open(req,timeout=18) as response:
        body=response.read(MAX_BYTES+1)
        if len(body)>MAX_BYTES:raise ValueError('response exceeds 2 MB limit')
        return response.status,response.geturl(),response.headers.get('Content-Type',''),body

def wildcard_delay(text):
    # robotparser can ignore a second wildcard group; use the strictest
    # applicable wildcard/our-agent delay across all groups.
    agents=[];seen_rule=False;values=[]
    for line in text.splitlines():
        line=line.split('#',1)[0].strip()
        if ':' not in line:continue
        key,value=(x.strip() for x in line.split(':',1));key=key.lower()
        if key=='user-agent':
            if seen_rule:agents=[];seen_rule=False
            agents.append(value.lower())
        else:
            seen_rule=True
            if key=='crawl-delay' and any(a=='*' or a in UA.lower() for a in agents):
                try:values.append(float(value))
                except ValueError:pass
    return max(values,default=0)

def robots_can_fetch(text,url):
    # Evaluate each applicable repeated group conservatively. Some robots files
    # repeat User-agent: * and robotparser alone checks only the first group.
    groups=[];agents=[];rules=[];seen_rule=False
    def flush():
        if agents and rules:groups.append((agents[:],rules[:]))
    for line in text.splitlines():
        line=line.split('#',1)[0].strip()
        if ':' not in line:continue
        key,value=(x.strip() for x in line.split(':',1));key=key.lower()
        if key=='user-agent':
            if seen_rule:flush();agents=[];rules=[];seen_rule=False
            agents.append(value.lower())
        else:
            seen_rule=True
            if key in ('allow','disallow'):rules.append(f'{key}: {value}')
    flush()
    for agents,rules in groups:
        if not any(a=='*' or a in UA.lower() for a in agents):continue
        rp=urllib.robotparser.RobotFileParser();rp.parse(['User-agent: *',*rules])
        if not rp.can_fetch(UA,url):return False
    return True

def retry_after_seconds(error):
    if error.code not in (429,503):return 0
    value=error.headers.get('Retry-After','') if error.headers else ''
    try:return max(300,float(value))
    except (TypeError,ValueError):
        try:return max(300,(email.utils.parsedate_to_datetime(value)-dt.datetime.now(dt.timezone.utc)).total_seconds())
        except (TypeError,ValueError,OverflowError):return 300

def stamp():return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')
def request_allowed(state,host):return time.time()>=state.get(host,{}).get('nextAllowed',0)
def save_state(state):write_json(CACHE/'host-state.json',state)
def reserve(state,host,delay):
    state[host]={'nextAllowed':time.time()+max(delay,0)};save_state(state)

def collect(source,start,end,run_dir,state):
    url=source.get('url','');host=host_of(url);sid=source.get('id',''); base={'sourceId':sid,'name':source.get('name',sid),'domain':host,'sourceUrl':url,'method':'deterministic-html','startedAt':stamp(),'outcome':'error','httpStatus':None,'candidateCount':0,'datedInWindow':0,'undatedCandidates':0,'windowStart':start,'windowEnd':end,'cacheKey':None,'sha256':None,'message':''}
    if not valid_source(source):
        base.update(outcome='configuration_error',message='Source URL or adapter is invalid.');return base
    rpath=CACHE/'robots'/f'{host}.json';robots=read_json(rpath,{})
    delay=max(1,float(source.get('minDelaySeconds',1)))
    if not robots or time.time()-robots.get('fetchedEpoch',0)>86400:
        if not request_allowed(state,host):base.update(outcome='deferred_rate_limit',message='Waiting for host request interval before robots check.');return base
        robots_url=urllib.parse.urljoin(url,'/robots.txt')
        try:
            reserve(state,host,delay);code,final,ctype,raw=fetch(robots_url)
            text=raw.decode('utf-8','replace');delay=max(delay,wildcard_delay(text));reserve(state,host,delay)
            robots={'fetchedEpoch':time.time(),'url':final,'text':text,'delay':delay};write_json(rpath,robots)
        except urllib.error.HTTPError as e:
            backoff=retry_after_seconds(e)
            if backoff:reserve(state,host,max(delay,backoff))
            base.update(outcome='robots_unavailable',httpStatus=e.code,message=f'Could not verify robots.txt (HTTP {e.code}).'+(' Retry deferred by server backoff.' if backoff else ''));return base
        except (urllib.error.URLError,TimeoutError,OSError,ValueError) as e:
            base.update(outcome='robots_unavailable',message=f'Could not verify robots.txt ({type(e).__name__}).');return base
    delay=max(delay,float(robots.get('delay',0)))
    if not robots_can_fetch(robots['text'],url):base.update(outcome='robots_disallowed',message='robots.txt disallows this collector for the source URL.');return base
    # Wait briefly for a normal one-second polite delay, but do not hold a run
    # open for a source with a longer required crawl delay.
    wait=state.get(host,{}).get('nextAllowed',0)-time.time()
    if wait>2:base.update(outcome='deferred_rate_limit',message=f'Polite delay: retry after {max(1,int(wait)+1)} seconds.');return base
    if wait>0:time.sleep(wait)
    try:
        reserve(state,host,delay);code,final,ctype,raw=fetch(url)
        base['httpStatus']=code;base['sha256']=hashlib.sha256(raw).hexdigest()
        if not ('text/html' in ctype.lower() or 'application/xhtml+xml' in ctype.lower()):
            base.update(outcome='unexpected_content',message='Response was not HTML.');return base
        rawfile=run_dir/(sid+'.html');rawfile.write_bytes(raw);base['cacheKey']=str(rawfile.relative_to(CACHE))
        decoded=raw.decode('utf-8','replace');rows=ADAPTERS[source['adapter']](decoded,final,start,end)
        candidate_path=run_dir/(sid+'.candidates.json');write_json(candidate_path,rows)
        # Publish only concise public candidate metadata; excerpts and raw HTML stay local.
        base['candidates']=candidate_summaries(rows)
        base['candidateCacheKey']=str(candidate_path.relative_to(CACHE))
        base.update(outcome='success' if rows else 'no_matches',candidateCount=len(rows),datedInWindow=sum(x.get('inWindow') is True for x in rows),undatedCandidates=sum(x.get('inWindow') is None for x in rows),message='Fetched and parsed public HTML; candidates require review.' if rows else 'Fetched HTML, but the adapter matched no candidate leads; inspect the cached page.')
    except urllib.error.HTTPError as e:
        backoff=retry_after_seconds(e)
        if backoff:reserve(state,host,max(delay,backoff))
        base.update(outcome='http_error',httpStatus=e.code,message=f'HTTP {e.code}; no bypass attempted.'+(' Retry deferred by server backoff.' if backoff else ''))
    except (urllib.error.URLError,TimeoutError,OSError,ValueError) as e:base.update(outcome='fetch_error',message=f'{type(e).__name__}: {str(e)[:180]}')
    except Exception as e:base.update(outcome='parser_error',message=f'{type(e).__name__}: {str(e)[:180]}')
    return base

def main():
    parser=argparse.ArgumentParser(description=__doc__);today=dt.datetime.now(TZ).date();parser.add_argument('--start-date',default=today.isoformat());parser.add_argument('--end-date',default=(today+dt.timedelta(days=30)).isoformat());parser.add_argument('--source',action='append',help='Source id; repeat for several. Defaults to all enabled sources.');parser.add_argument('--reparse-run',help='Reparse HTML from an existing local run without making network requests; requires --source.')
    args=parser.parse_args()
    if args.reparse_run and not args.source:parser.error('--reparse-run requires at least one --source')
    start=dt.date.fromisoformat(args.start_date).isoformat();end=dt.date.fromisoformat(args.end_date).isoformat()
    if start>end:parser.error('start date must be on or before end date')
    config=read_json(CONFIG,{});all_sources=config.get('sources',[])
    ids=[s.get('id') for s in all_sources]
    if len(ids)!=len(set(ids)) or any(not isinstance(x,str) for x in ids):parser.error('source registry contains missing or duplicate ids')
    selected=[s for s in all_sources if s.get('enabled') and (not args.source or s['id'] in args.source)]
    missing=set(args.source or [])-{s['id'] for s in selected}
    if missing:parser.error('unknown or disabled source: '+', '.join(sorted(missing)))
    CACHE.mkdir(parents=True,exist_ok=True)
    lock=(CACHE/'collector.lock').open('a')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:
        print('Another collector run is active; no requests were made.');return 2
    runid=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');run_dir=CACHE/'runs'/runid;run_dir.mkdir(parents=True,exist_ok=False)
    run_started=stamp();state=read_json(CACHE/'host-state.json',{});results=[]
    for s in selected:
        result=reparse(s,start,end,run_dir,args.reparse_run) if args.reparse_run else collect(s,start,end,run_dir,state);results.append(result)
        print(f"{s['id']}: {result['outcome']} · {result['candidateCount']} candidates · {result['datedInWindow']} dated in window")
    run={'id':runid,'startedAt':run_started,'completedAt':stamp(),'windowStart':start,'windowEnd':end,'results':results}
    write_json(run_dir/'run.json',run)
    history=read_json(HISTORY,[]);history.append(run);write_json(HISTORY,history)
    print(f'Run {runid}; inspect .collector-cache/runs/{runid}/run.json for local snapshot and candidate paths.')
    return 0 if all(x['outcome'] in ('success','no_matches','deferred_rate_limit') for x in results) else 1
if __name__=='__main__':raise SystemExit(main())
