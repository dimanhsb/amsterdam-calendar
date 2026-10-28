#!/usr/bin/env python3
"""Join the full saved source inventory with explicit collector run outcomes."""
import datetime as dt, importlib.util, json
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1]
def read(path,default):
 p=ROOT/path
 return json.loads(p.read_text(encoding='utf-8')) if p.exists() else default
spec=importlib.util.spec_from_file_location('source_guides',ROOT/'scripts/source-guides.py');guides=importlib.util.module_from_spec(spec);spec.loader.exec_module(guides)
inventory=guides.load_sources()
registry=read('data/collector-sources.json',{}).get('sources',[])
runs=read('data/collection-runs.json',[])
audit=read('data/source-audit.json',{});audit_by={x['domain']:x for x in audit.get('sources',[])}
report=read('data/research-report.json',{});yield_by={x['domain']:x for x in report.get('websites',[])}
evidence={s['url'] for s in read('data/sources.json',[]) if s.get('url')}
by_id=defaultdict(list)
for run in runs:
 for result in run.get('results',[]):
  by_id[result['sourceId']].append({'runId':run['id'],**result})
endpoints=[]
for s in registry:
 if not s.get('enabled'):continue
 history=by_id[s['id']];last=history[-1] if history else None;success=next((x for x in reversed(history) if x.get('outcome')=='success'),None)
 endpoints.append({'id':s['id'],'name':s['name'],'url':s['url'],'domain':(urlparse(s['url']).hostname or '').lower().removeprefix('www.'),'method':'deterministic-html','adapter':s['adapter'],'note':s.get('note',''),'lastAttempt':last,'lastSuccess':success,'lastSuccessAt':(success.get('sourceFetchedAt') or success.get('startedAt')) if success else None,'recentAttempts':history[-5:][::-1]})
for domain in audit_by:inventory.setdefault(domain,[])
for domain in yield_by:inventory.setdefault(domain,[])
for endpoint in endpoints:inventory.setdefault(endpoint['domain'],[])
rows=[]
for domain,items in sorted(inventory.items()):
 a=audit_by.get(domain);y=yield_by.get(domain,{});configured=[e['id'] for e in endpoints if e['domain']==domain]
 refs=[];seen=set()
 for entry in items:
  url=entry.get('url','');parts=urlparse(url)
  if parts.scheme not in ('http','https') or not parts.hostname or url in seen:continue
  seen.add(url);kind='recorded evidence' if url in evidence else ('held lead' if entry.get('heldContexts') else ('historical audit' if str(entry.get('type','')).startswith('Historical audit') else ('new source proposal' if entry.get('discoveryContexts') else 'research / idea lead')))
  refs.append({'url':url,'title':entry.get('title') or domain,'kind':kind,'heldContexts':entry.get('heldContexts',[]),'discoveryContexts':entry.get('discoveryContexts',[])})
 refs.sort(key=lambda x:(x['title'].casefold(),x['url']))
 rows.append({'domain':domain,'guide':next((name for name in [a.get('guide') if a else None,guides.filename(domain)] if name and (ROOT/'source-guides'/name).is_file()),None),'references':refs,'evidenceUrls':sum(x['kind']=='recorded evidence' for x in refs),'leadUrls':sum(x['kind']!='recorded evidence' for x in refs),'configuredSources':configured,'routeAssessment':f'{len(configured)} configured entry point(s); other pages unassessed' if configured else 'not assessed for automation','historicalAudit':{'checkedAt':audit.get('checkedAt'),'outcome':a.get('outcome'),'method':a.get('bestMethod'),'issue':a.get('issue')} if a else None,'historicalPrimaryEvents':y.get('primaryEvents',0)})
latest=[e['lastAttempt']['outcome'] if e['lastAttempt'] else 'not_run' for e in endpoints]
result={'generatedAt':dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'),'summary':{'websites':len(rows),'referenceUrls':sum(len(r['references']) for r in rows),'evidenceUrls':len(evidence),'configuredSources':len(endpoints),'success':latest.count('success'),'noMatches':latest.count('no_matches'),'deferred':latest.count('deferred_rate_limit'),'failed':sum(x not in ('success','no_matches','deferred_rate_limit','not_run') for x in latest),'notRun':latest.count('not_run'),'historicAuditSites':len(audit_by)},'endpoints':endpoints,'recentRefreshes':read('data/refresh-runs.json',[])[-20:][::-1],'websites':rows}
p=ROOT/'data/collection-status.json';p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Collection inventory:',json.dumps(result['summary']))
