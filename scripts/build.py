import pathlib,json,shutil,subprocess,sys,hashlib,os
from datetime import datetime,date
from zoneinfo import ZoneInfo
R=pathlib.Path(__file__).resolve().parents[1]; D=R/'dist';D.mkdir(exist_ok=True)
# Public release uses the checked-in research summaries; the private evidence archive is not bundled.
profile=json.loads((R/'data/preferences.json').read_text())
(R/'profile.js').write_text('// Generated from data/preferences.json by scripts/build.py.\nexport const DEFAULT_PROFILE = '+json.dumps(profile,ensure_ascii=False,separators=(',',':'))+';\n')
for name in ['index.html','styles.css','app.js','core.js','icons.js','preferences.js','profile.js','catalog.js']:
 shutil.copyfile(R/name,D/name)
data={key:json.loads((R/'data'/f'{key}.json').read_text()) for key in ['events','ideas','sources','offers']}
data['meta']=json.loads((R/'data/meta.json').read_text())
data['preferences']=profile
if (R/'data/idea-catalog.json').exists():data['ideaCatalog']=json.loads((R/'data/idea-catalog.json').read_text())
report=R/'data/research-report.json'
if report.exists():data['report']=json.loads(report.read_text())
audit=R/'data/source-audit.json'
if audit.exists():data['sourceAudit']=json.loads(audit.read_text())
collection=R/'data/collection-status.json'
if collection.exists():data['collectionStatus']=json.loads(collection.read_text())
priorities=R/'data/source-priority.json'
if priorities.exists():data['sourcePriority']=json.loads(priorities.read_text())
# Publish only current/future occurrences; canonical research remains local for deduplication.
as_of=os.environ.get('CALENDAR_AS_OF') or datetime.now(ZoneInfo('Europe/Amsterdam')).date().isoformat()
assert date.fromisoformat(as_of).isoformat()==as_of
all_events=data['events']
def keep(event):
 stamp=(event.get('end') or event.get('start')) if event.get('status')=='dated' else event.get('proposedDate')
 return not stamp or stamp[:10]>=as_of
data['events']=[event for event in all_events if keep(event)]
data['meta']['publishedAsOf']=as_of
data['meta']['archivedPastCount']=len(all_events)-len(data['events'])
(D/'data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
shutil.copytree(R/'prompts',D/'prompts',dirs_exist_ok=True)
if (R/'source-guides').exists():shutil.copytree(R/'source-guides',D/'source-guides',dirs_exist_ok=True)
print(f"Built {len(data['events'])} events, {len(data['ideas'])} ideas, {len(data['sources'])} sources")

shutil.copyfile(R/'manifest.webmanifest',D/'manifest.webmanifest')
shutil.copyfile(R/'favicon.ico',D/'favicon.ico')
shutil.copytree(R/'icons',D/'icons',dirs_exist_ok=True)
assets=['index.html','styles.css','app.js','core.js','icons.js','preferences.js','profile.js','catalog.js','data.json','manifest.webmanifest','icons/app-192.png','icons/app-512.png','icons/amsterdam-calendar.svg','icons/amsterdam-192.png','icons/amsterdam-512.png','icons/amsterdam-32.png','icons/amsterdam-touch.png','icons/app.svg','icons/calendar.svg','icons/favicon-32.png','icons/apple-touch-icon.png','favicon.ico','prompts/discover-more.md']
identity=hashlib.sha256(b''.join((D/asset).read_bytes() for asset in assets)).hexdigest()[:16]
(D/'sw.js').write_text((R/'sw.template.js').read_text().replace('__BUILD_ID__',identity).replace('__ASSETS__',json.dumps(assets)))
print(f"Live data: {len(data['events'])} records; {data['meta']['archivedPastCount']} past records excluded as of {as_of}. Cache {identity}")
