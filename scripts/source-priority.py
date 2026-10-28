#!/usr/bin/env python3
"""Generate evidence-based source queues; no network access or model calls."""
import datetime as dt, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def read(name):return json.loads((ROOT/name).read_text(encoding='utf-8'))
c=read('data/collection-status.json');policy=read('data/source-priority-policy.json');profile=read('data/preferences.json')
focus={x['domain']:(i,x['reason'],x.get('entryUrls',[])) for i,x in enumerate(policy['focus'])}
endpoint_by_id={e['id']:e for e in c['endpoints']}
queues={'deterministic':[],'code_assessment':[],'luna':[],'harder':[],'unassessed':[],'excluded':[]}
for w in c['websites']:
 domain=w['domain'];audit=w.get('historicalAudit');outcome=audit.get('outcome') if audit else None;method=audit.get('method') if audit else None
 endpoints=[endpoint_by_id[x] for x in w['configuredSources'] if x in endpoint_by_id]
 successes=[e for e in endpoints if e.get('lastSuccess')]
 last=[e.get('lastAttempt') for e in endpoints if e.get('lastAttempt')]
 priority,reason,preferred_urls=focus.get(domain,(len(focus)+1,'',[]));yield_count=w.get('historicalPrimaryEvents',0)
 urls=preferred_urls[:3] if preferred_urls else list(dict.fromkeys(r['url'] for r in w['references'] if not r.get('heldContexts')))[:3]
 if not urls:urls=[r['url'] for r in w['references']][:3]
 base={'domain':domain,'guide':w.get('guide'),'focusRank':priority,'focusReason':reason,'historicalDatedEvents':yield_count,'referenceCount':len(w['references']),'entryUrls':urls,'audit':audit,'endpointIds':[e['id'] for e in endpoints],'lastOutcomes':[{'sourceId':e['id'],'outcome':e.get('lastAttempt',{}).get('outcome') if e.get('lastAttempt') else 'not_run','httpStatus':e.get('lastAttempt',{}).get('httpStatus') if e.get('lastAttempt') else None,'message':e.get('lastAttempt',{}).get('message','') if e.get('lastAttempt') else '','lastSuccessAt':e.get('lastSuccessAt'),'lastSuccessCacheKey':(e.get('lastSuccess') or {}).get('cacheKey'),'lastSuccessCandidateKey':(e.get('lastSuccess') or {}).get('candidateCacheKey')} for e in endpoints]}
 if outcome=='excluded':
  queues['excluded'].append({**base,'classification':'excluded','nextAction':'Skip under the current blacklist; retain historical evidence.'});continue
 if endpoints:
  proven=bool(successes)
  if any((x.get('httpStatus')==429 or '429' in x.get('message','')) for x in last if x):
   action='Rate limited: wait for the recorded backoff; do not use a model or browser to evade it. Review saved evidence or an independent permitted source.'
  elif proven and any(x.get('outcome') not in ('success','no_matches') for x in last if x):
   action='Retry the configured collector only after its recorded delay; retain and review the last successful snapshot.'
  elif proven:
   action='Run the configured collector or reparse a saved snapshot; verify candidates before calendar import.'
  else:action='Probe the configured public endpoint and inspect a saved response; this adapter is not yet proven.'
  execution_rank=3 if any((x.get('httpStatus')==429 or '429' in x.get('message','')) for x in last if x) else (1 if proven and any(x.get('outcome') not in ('success','no_matches') for x in last if x) else (0 if proven else 2))
  queues['deterministic'].append({**base,'executionRank':execution_rank,'classification':'code_verified' if proven else 'code_unverified','nextAction':action,'evidence':'A configured adapter has extracted candidates from public HTML or a saved public snapshot.' if proven else 'An adapter is configured, but no successful candidate extraction has been recorded.'})
 else:
  code_action=('Historical access restriction: use saved evidence or a permitted alternative; do not repeat or bypass the gated route without a relevant change.' if outcome=='blocked' else 'Inspect prior limitations, then check for an allowed public feed or stable HTML with a bounded probe before using a model.')
  queues['code_assessment'].append({**base,'classification':'unassessed_for_code','nextAction':code_action})
 if not successes and outcome in ('usable','partial') and method in ('web-extraction','desktop-browser','android-firefox','android-app'):
  luna_action=('Rate limited: wait for backoff; never use Luna or a browser to evade it. Only assess the Luna fallback after permitted code access is resolved.' if any((x.get('httpStatus')==429 or '429' in x.get('message','')) for x in last if x) else 'After a permitted code assessment shows a gap, use the short source brief with Luna; verify dates, costs, language, and access.')
  queues['luna'].append({**base,'classification':'historical_luna_candidate','nextAction':luna_action, 'evidence':f"18 October Luna audit: {outcome} via {method}; this was a spot check, not a current guarantee."})
 elif not successes and outcome in ('blocked','unavailable'):
  queues['harder'].append({**base,'classification':'unresolved_access_or_coverage','nextAction':'Review the prior failure and assess permitted alternatives. A stronger model cannot bypass a gate; escalate only unresolved interpretation or ordinary rendering after cheaper methods.', 'evidence':f"18 October Luna audit: {outcome} via {method}; the cause and freshness need rechecking."})
 elif not endpoints and not audit:
  queues['unassessed'].append({**base,'classification':'unassessed','nextAction':'Assess deterministic collection first; then record which fallback, if any, worked.'})
def key(x):return (x['focusRank'],-x['historicalDatedEvents'],x['domain'])
for name,items in queues.items():items.sort(key=(lambda x:(x.get('executionRank',0),*key(x))) if name=='deterministic' else key)
result={'generatedAt':dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'),'order':['deterministic','code_assessment','luna','harder','discovery'],'policy':'Run deterministic collectors and assess public structured routes first; use Luna only for the unresolved extraction; escalate conflicts or rendering only when needed. A rate limit or access restriction is not permission to bypass it.','caveat':'Historical yield is cumulative, can include past events or duplicates, and is a prioritization clue, not a current success rate. Luna candidates are historical spot checks; unassessed code routes may still work. Queues can overlap by design.','summary':{k:len(v) for k,v in queues.items()},'queues':queues,'discovery':policy['discovery'],'blacklist':profile.get('blacklist',[])}
(ROOT/'data/source-priority.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Source priorities:',json.dumps(result['summary']))
