#!/usr/bin/env python3
"""Print the prioritized source queue or a small Luna source brief; no network/model calls."""
import argparse,datetime as dt,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--queue',choices=['deterministic','code_assessment','luna','harder','unassessed','excluded','discovery','all'],default='deterministic')
p.add_argument('--limit',type=int,default=20);p.add_argument('--json',action='store_true');p.add_argument('--brief',metavar='DOMAIN');p.add_argument('--find',metavar='TEXT',help='Search the saved source and held-lead inventory without network access');p.add_argument('--start-date',type=dt.date.fromisoformat);p.add_argument('--end-date',type=dt.date.fromisoformat)
a=p.parse_args()
if a.limit<1:p.error('--limit must be positive')
if a.find and a.brief:p.error('--find and --brief cannot be combined')
d=json.loads((ROOT/'data/source-priority.json').read_text());profile=json.loads((ROOT/'data/preferences.json').read_text())
if a.find:

 status=json.loads((ROOT/'data/collection-status.json').read_text());q=a.find.casefold();matches=[]
 for site in status['websites']:
  refs=[r for r in site['references'] if q in (r['title']+' '+r['url']+' '+' '.join(x.get('reason','') for x in r.get('heldContexts',[]))+' '+' '.join(x.get('nextStep','') for x in r.get('discoveryContexts',[]))).casefold()]
  if q in site['domain'].casefold() or refs:matches.append({'domain':site['domain'],'guide':site['guide'],'matchingReferences':refs if refs else site['references'][:3]})
 matches=matches[:a.limit]
 if a.json:print(json.dumps(matches,ensure_ascii=False,indent=2))
 else:
  for site in matches:
   print('\n'+site['domain']+' · '+str(site['guide'] or 'no guide'))
   for ref in site['matchingReferences'][:5]:print('  '+ref['kind']+': '+ref['title']+' · '+ref['url'])
elif a.brief:
 if not a.start_date or not a.end_date or a.start_date>a.end_date:p.error('--brief requires valid --start-date and --end-date')
 candidates=[x for xs in d['queues'].values() for x in xs if x['domain']==a.brief.lower().removeprefix('www.')]
 if not candidates:p.error('domain not found in source inventory')
 if any(x['classification']=='excluded' for x in candidates):p.error('source is excluded by the saved blacklist')
 row=next((x for x in candidates if x['classification']=='historical_luna_candidate'),candidates[0]);audit=row.get('audit') or {}
 print(f"Luna research brief — {row['domain']} · {a.start_date} to {a.end_date}")
 print('Use the deterministic collector and code feasibility assessment first. If a rate limit or access gate appears, stop rather than bypassing it.')
 print('Guide:',('source-guides/'+row['guide']) if row.get('guide') else 'not yet available')
 print('Saved public references (may be stale or incidental):', ' ; '.join(row['entryUrls']) or 'none')
 print('Historical audit:',audit.get('checkedAt','not audited'),audit.get('outcome','unknown'),audit.get('method','unknown'))
 print('Known finding:',audit.get('issue','No historical audit evidence; inspect a source guide and log uncertainty.'))
 print('Priority action:',row.get('nextAction','Assess the public code route first.'))
 for attempt in row.get('lastOutcomes',[]):
  print('Latest code attempt:',attempt['sourceId'],attempt['outcome'],attempt.get('message',''))
  for label,key in [('Last successful HTML','lastSuccessCacheKey'),('Last successful candidate data','lastSuccessCandidateKey')]:
   rel=attempt.get(key)
   if not rel:continue
   path=(ROOT/'.collector-cache'/rel).resolve()
   if path.is_relative_to((ROOT/'.collector-cache').resolve()) and path.is_file():print(label+':',path)
   else:print(label+': not available on this machine')
 print('Read prompts/luna-source-refresh.md and any relevant local cached candidate file. Research only one source; return a small batch of individually evidenced dates, times, location, prices/extras, language, single-visit eligibility and availability. Save unknowns and failures. Do not invent recurrences or assume page language is spoken language.')
 print('Preferred:',profile['timezone'],'weekends any time; weekdays from',profile['weekdayEveningStart'],'or same-day mornings ending by',profile['weekdayMorningEnd'])
 print('Blacklist:',', '.join(profile.get('blacklist',[])),'; do not book, RSVP, contact, pay, sign in, or bypass gates.')
else:
 names=list(d['queues']) if a.queue=='all' else ([] if a.queue=='discovery' else [a.queue]);out={k:d['queues'][k][:a.limit] for k in names}
 if a.queue=='discovery':out={'discovery':d['discovery'][:a.limit]}
 if a.json:print(json.dumps(out,ensure_ascii=False,indent=2))
 else:
  for name,items in out.items():
   print(f'\n{name} ({len(items)} shown)')
   for x in items:
    if name=='discovery':print(f"- {x['title']}: {x['steps']}")
    else:print(f"- {x['domain']} · {x['classification']} · {x['historicalDatedEvents']} historical dated events: {x['nextAction']}")
