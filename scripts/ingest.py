"""Validate and add evidence batches without regenerating occurrences.
Default is a dry run. --apply writes only after validation; conflicting updates
are held unless --allow-updates follows a human/agent evidence review.
"""
import argparse,copy,datetime as dt,json,pathlib,re,unicodedata,math
from urllib.parse import urlparse
from zoneinfo import ZoneInfo
R=pathlib.Path(__file__).resolve().parents[1];TZ=ZoneInfo('Europe/Amsterdam')
def read(name):return json.loads((R/'data'/f'{name}.json').read_text())
def norm(s):return re.sub(r'[^a-z0-9]+',' ',unicodedata.normalize('NFKD',str(s)).encode('ascii','ignore').decode().lower()).strip()
PROFILE=read('preferences')
RULES={'climbing':r'\b(?:climb(?:ing)?|boulder(?:ing|s)?|bouldergym|klimmuur)\b','circus-acrobatics':r'\b(?:circus|acrobat(?:ic|ics)?|acro.?yoga|aerial|pole(?: dance| fitness)?|juggling|handstand|object.manipulation)\b'}
def blocked(item):
 text=' '.join([item.get('title',item.get('name','')),item.get('category','')]).lower()
 return item.get('status')=='excluded' or any(re.search(RULES[k],text,re.I) for k in PROFILE['blacklist'] if k in RULES) or any(k.lower() in text for k in PROFILE.get('customKeywords',[]))
def preferred(e):
 if not e.get('start'):return False
 start=dt.datetime.fromisoformat(e['start']).astimezone(TZ)
 if PROFILE.get('weekends',True) and start.weekday()>=5:return True
 if start.strftime('%H:%M')>=PROFILE['weekdayEveningStart']:return True
 if start.strftime('%H:%M')<PROFILE['weekdayMorningEnd'] and e.get('end'):
  end=dt.datetime.fromisoformat(e['end']).astimezone(TZ)
  return end.date()==start.date() and end.strftime('%H:%M')<=PROFILE['weekdayMorningEnd'] and end>start
 return False
def safe(url):
 if not isinstance(url,str):return False
 p=urlparse(url)
 return (p.scheme in ('https','http') and bool(p.hostname)) or (p.scheme=='mailto' and '@' in p.path)
def fingerprint(e):return (norm(e.get('title','')),e.get('start'),norm(e.get('venue','')))
def load_batch(path):
 p=pathlib.Path(path);p=p if p.is_absolute() else R/p
 return p,json.loads(p.read_text())
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('batches',nargs='+');ap.add_argument('--apply',action='store_true');ap.add_argument('--allow-updates',action='store_true');ap.add_argument('--log',help='Write a sanitized JSON decision log');a=ap.parse_args()
 data={n:read(n) for n in ['events','sources','offers','ideas']};meta=read('meta');byid={n:{r['id']:r for r in data[n]} for n in ['events','offers','ideas']};byurl={s['url']:s for s in data['sources']}
 decisions=[];errors=[]
 for filename in a.batches:
  path,batch=load_batch(filename);roundid=batch.get('researchRound') or next((e.get('researchRound') for e in batch.get('events',[]) if e.get('researchRound')),path.stem)
  report={'batch':str(path.relative_to(R)) if path.is_relative_to(R) else path.name,'round':roundid,'newEventIds':[],'newDatedIds':[],'promotedEventIds':[],'newPreferredIds':[],'newOfferIds':[],'newIdeaIds':[],'duplicates':[],'blacklisted':[],'heldUpdates':[],'sourceCount':0,'sourceUpdates':[],'linkChanges':[],'reviewUpdates':[],'attempts':batch.get('attempts',[])}
  for source in batch.get('sources',[]):
   source=copy.deepcopy(source)
   if not all(source.get(k) for k in ['title','url','type','evidence','checkedAt']) or not safe(source['url']):errors.append(f'{path.name}: invalid source {source.get("url")}');continue
   old=byurl.get(source['url'])
   if old:
    # Keep both observations instead of silently erasing historical limitations.
    if source['evidence'] not in old['evidence']:
     report['sourceUpdates'].append(source['url'])
     old.setdefault('observations',[]).append({'checkedAt':source['checkedAt'],'evidence':source['evidence']})
     old['evidence']+=' Follow-up: '+source['evidence']
    old['checkedAt']=max(old['checkedAt'],source['checkedAt'])
   else:
    nums=[int(m.group(1)) for s in byurl.values() if (m:=re.fullmatch(r'source-(\d+)',s['id']))]
    source['id']=f'source-{max(nums,default=0)+1:03d}';byurl[source['url']]=source;report['sourceCount']+=1
  for kind,key in [('ideas','newIdeas'),('events','events'),('offers','offers')]:
   for incoming in batch.get(key,[]):
    row=copy.deepcopy(incoming);identity=row.get('id')
    if not identity:errors.append(f'{path.name}: missing {kind} id');continue
    if blocked(row):report['blacklisted'].append(identity);continue
    if kind in ('events','offers'):
     urls=row.get('sourceUrls',[])
     if isinstance(urls,str):urls=[urls]
     if not isinstance(urls,list) or any(not isinstance(u,str) for u in urls):errors.append(f'{identity}: sourceUrls must be a list of URL strings');continue
     row['sourceUrls']=list(dict.fromkeys(urls))
     missing=[u for u in urls if u not in byurl or not safe(u)]
     if not urls or missing:errors.append(f'{identity}: missing/unsafe registered sources {missing}');continue
     if not safe(row.get('bookingUrl','')):errors.append(f'{identity}: invalid booking URL');continue
     evidence=row.get('evidence',{})
     if isinstance(evidence,str):row['evidence']={'observations':evidence}
     elif isinstance(evidence,list):row['evidence']={'observations':' '.join(map(str,evidence))}
     if not isinstance(row.get('evidence'),dict):errors.append(f'{identity}: evidence must be object');continue
     row.setdefault('languages',[])
     if 'languages' in row and (not isinstance(row['languages'],list) or any(not isinstance(c,str) or not re.fullmatch('[a-z]{2,3}',c) for c in row['languages'])):errors.append(f'{identity}: languages must be explicit ISO codes or an empty array');continue
     row.setdefault('researchRound',roundid)
     if row.get('participation')=='passive':row['participation']='audience'
     if kind=='events' and row.get('availability') not in ['unchecked','available','sold-out','waitlist','cancelled','conflict']:errors.append(f'{identity}: invalid availability');continue
     row.setdefault('discoverySource',row['sourceUrls'][0])
     if not safe(row['discoverySource']) or urlparse(row['discoverySource']).scheme not in ('http','https'):
      errors.append(f'{identity}: discoverySource must be an actual public page URL');continue
     if row.get('researchMethod') not in ['web-extraction','desktop-browser','android-firefox','android-app','official-feed','manual-unknown']:
      errors.append(f'{identity}: researchMethod must name the actual observed route');continue
     if kind=='events':
      required=['title','status','timezone','category','area','venue','description','participation','attendance','language','dateEvidence','checkedAt','availability','price','uncertainties']
      if any(k not in row for k in required):errors.append(f'{identity}: incomplete event schema');continue
      if row['status'] not in ['dated','lead']:errors.append(f'{identity}: invalid event status');continue
      if row['timezone']!='Europe/Amsterdam':errors.append(f'{identity}: invalid IANA timezone');continue
      price=row['price'];amount=price.get('amount') if isinstance(price,dict) else None
      if not isinstance(price,dict) or any(k not in price for k in ['amount','type','from','note','caption']) or (amount is not None and (isinstance(amount,bool) or not isinstance(amount,(int,float)) or not math.isfinite(amount) or amount<0)) or ((amount==0)!=(price.get('type')=='free')):errors.append(f'{identity}: invalid price; unknown is null, zero is explicitly free');continue
      if row['status']=='dated':
       try:
        start=dt.datetime.fromisoformat(row['start'])
        if start.tzinfo is None or not meta['coverageStart']<=start.date().isoformat()<=meta['coverageEnd']:raise ValueError('range or timezone')
        if start.astimezone(TZ).strftime('%Y-%m-%dT%H:%M')!=start.strftime('%Y-%m-%dT%H:%M'):raise ValueError('Amsterdam offset')
        if row.get('end'):
         end=dt.datetime.fromisoformat(row['end'])
         if end.tzinfo is None or end<=start or end.astimezone(TZ).strftime('%Y-%m-%dT%H:%M')!=end.strftime('%Y-%m-%dT%H:%M'):raise ValueError('end offset or instant')
       except (ValueError,TypeError,KeyError):errors.append(f'{identity}: invalid exact date/time');continue
      elif row.get('start') is not None:errors.append(f'{identity}: lead must not have inferred start');continue
      if not row.get('address') and not any(re.search(r'address|meeting point',u,re.I) for u in row['uncertainties']):row['uncertainties'].append('Exact street address or meeting point was not published in the checked listing; confirm with the organizer.')
      duplicate=next((old for old in byid['events'].values() if old['id']!=identity and fingerprint(old)==fingerprint(row)),None)
      if duplicate:
       report['duplicates'].append({'candidate':identity,'existing':duplicate['id']});continue
     else:
      required=['name','venue','category','area','description','attendance','language','directPrice','scheduleHorizon','checkedAt','uncertainties']
      if any(k not in row for k in required):errors.append(f'{identity}: incomplete offer schema');continue
      if row.get('start'):errors.append(f'{identity}: offer must stay undated');continue
      duplicate=next((old for old in byid['offers'].values() if old['id']!=identity and norm(old['name'])==norm(row['name']) and norm(old['venue'])==norm(row['venue'])),None)
      if duplicate:report['duplicates'].append({'candidate':identity,'existing':duplicate['id']});continue
    old=byid[kind].get(identity)
    if old:
     if row==old:continue
     if not a.allow_updates:report['heldUpdates'].append(identity);continue
     if kind=='events' and old.get('start')!=row.get('start') and not (old['status']=='lead' and row['status']=='dated'):errors.append(f'{identity}: changed published instant requires manual reconciliation');continue
     if kind=='events' and old.get('status')!='dated' and row.get('status')=='dated':
      report['promotedEventIds'].append(identity)
      if preferred(row):report['newPreferredIds'].append(identity)
     byid[kind][identity]=row
    else:
     byid[kind][identity]=row
     report[{'events':'newEventIds','offers':'newOfferIds','ideas':'newIdeaIds'}[kind]].append(identity)
     if kind=='events' and row['status']=='dated':
      report['newDatedIds'].append(identity)
      if preferred(row):report['newPreferredIds'].append(identity)
  for kind,key in [('events','eventIdeaLinks'),('offers','offerIdeaLinks')]:
   for identity,links in batch.get(key,{}).items():
    if identity not in byid[kind] or not isinstance(links,list) or any(i not in byid['ideas'] for i in links):errors.append(f'{identity}: invalid explicit idea links');continue
    oldlinks=byid[kind][identity].get('ideaIds',[]);added=[i for i in links if i not in oldlinks]
    if added:report['linkChanges'].append({'kind':kind,'id':identity,'added':added})
    byid[kind][identity]['ideaIds']=list(dict.fromkeys([*oldlinks,*links]))
  if batch.get('priceUpdates'):errors.append(f'{path.name}: priceUpdates require a reviewed full-record update; no partial price overwrite applied')
  for review in batch.get('ideaReviews',[]):
   if review.get('ideaId') in byid['ideas']:
    idea=byid['ideas'][review['ideaId']];update={**review,'checkedAt':batch['checkedAt']}
    if idea.get('research')!=update:
     report['reviewUpdates'].append({'id':idea['id'],'held':not a.allow_updates})
     if a.allow_updates:
      if idea.get('research'):idea.setdefault('researchHistory',[]).append(idea['research'])
      idea['research']=update
  decisions.append(report)
 result={'mode':'apply' if a.apply else 'dry-run','decisions':decisions,'errors':errors}
 if a.log:
  out=pathlib.Path(a.log);out=out if out.is_absolute() else R/out;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
 for d in decisions:print(f"{d['round']}: {len(d['newEventIds'])} new events ({len(d['newPreferredIds'])} preferred), {len(d['newOfferIds'])} offers, {len(d['duplicates'])} duplicates, {len(d['blacklisted'])} blacklisted, {len(d['heldUpdates'])} updates held, {len(d['linkChanges'])} link changes, {len(d['sourceUpdates'])} source observations")
 if errors:
  for e in errors:print('ERROR:',e)
  raise SystemExit(1)
 if a.apply:
  for n in ['events','offers','ideas']:data[n]=list(byid[n].values())
  data['events'].sort(key=lambda e:(e.get('start') or e.get('proposedDate') or '',e['id']));data['sources']=list(byurl.values())
  for n,rows in data.items():(R/'data'/f'{n}.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
  print('Applied validated additions. Run build and scripts/check.mjs before publishing.')
if __name__=='__main__':main()
