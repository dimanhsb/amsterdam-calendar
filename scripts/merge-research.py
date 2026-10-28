"""Merge audited batches, preserving saved IDs and distinguishing dates from offers."""
import sys,json,pathlib
R=pathlib.Path(__file__).resolve().parents[1]
def read(name):return json.loads((R/'data'/f'{name}.json').read_text())
by_id={e['id']:e for e in read('events')};by_url={s['url']:s for s in read('sources')}
by_offer={o['id']:o for o in read('offers')};ideas=read('ideas');by_idea={i['id']:i for i in ideas}
def source(item):
 old=by_url.get(item['url']);by_url[item['url']]={**item,'id':old['id'] if old else 'source-%03d'%(len(by_url)+1)}
def urls(item):
 if isinstance(item.get('sourceUrls'),str):item['sourceUrls']=[item['sourceUrls']]
 item['sourceUrls']=list(dict.fromkeys(item['sourceUrls']))
 if not item.get('bookingUrl'):item['bookingUrl']=item['sourceUrls'][0]
def evidence(item):
 value=item.get('evidence',{})
 if isinstance(value,str):item['evidence']={'summary':value}
 elif isinstance(value,list):item['evidence']={'observations':' '.join(str(x) for x in value)}
def cover(item,kind):
 for url in item['sourceUrls']:
  if url not in by_url:
   if kind!='lead':raise ValueError('Missing source '+url+' for '+item.get('id',item.get('eventId','')))
   source({'url':url,'title':item['title']+' · unverified lead','type':'Unverified discovery lead','evidence':'Not verified as a dated attendance option. See the lead record for evidence limitations.','checkedAt':item['checkedAt']})
for filename in sys.argv[1:]:
 batch=json.loads((R/filename).read_text())
 for item in batch.get('sources',[]):source(item)
 for event in batch.get('events',[]):
  event=dict(event);urls(event);evidence(event)
  if event.get('participation')=='class':event['participation']='active'
  if not event.get('venue'):event['venue']='Venue to confirm'
  if not event.get('address'):
   note='Exact street address or meeting point was not published in the opened listing; confirm with the organizer.'
   event['uncertainties']=list(dict.fromkeys([*event.get('uncertainties',[]),note]))
  old=by_id.get(event['id'])
  promotion=old and old['status']=='lead' and not old.get('start') and event['status']=='dated' and event.get('dateEvidence')
  if old and old.get('start')!=event.get('start') and not promotion:raise ValueError('Conflicting start for '+event['id'])
  cover(event,event['status']);by_id[event['id']]=event
 for update in batch.get('priceUpdates',[]):
  e=by_id[update['eventId']];cover(update,'price update');e['price']=update['price']
  e['sourceUrls']=list(dict.fromkeys([*update['sourceUrls'],*e['sourceUrls']]))
  e['checkedAt']=update.get('checkedAt',batch['checkedAt'])
  e['evidence']={k:v for k,v in e.get('evidence',{}).items() if not (('price' in k or 'fee' in k) and any(t in str(v).lower() for t in ['unknown','not stated','not observed','not verified']))}
  e['evidence'].update(update.get('evidence',{}))
  e['uncertainties']=list(dict.fromkeys([*[u for u in e['uncertainties'] if not any(t in u.lower() for t in ['price','fee','cost'])],*update.get('uncertainties',[])]))
 for offer in batch.get('offers',[]):
  offer=dict(offer);urls(offer);evidence(offer)
  if offer.get('classpass') and not offer['classpass'].get('url'):offer['classpass']=None
  cover(offer,'offer');by_offer[offer['id']]=offer
 for review in batch.get('ideaReviews',[]):
  if review['ideaId'] not in by_idea:raise ValueError('Unknown idea '+review['ideaId'])
  by_idea[review['ideaId']]['research']={**review,'checkedAt':batch['checkedAt']}
overrides=R/'data/research-overrides.json'
if overrides.exists():
 for key,fields in json.loads(overrides.read_text()).items():
  if key not in by_id:raise ValueError('Unknown override '+key)
  by_id[key].update(fields)
rows=sorted(by_id.values(),key=lambda e:(e.get('start') or e.get('proposedDate') or '',e['id']))
for name,value in [('events',rows),('sources',list(by_url.values())),('offers',list(by_offer.values())),('ideas',ideas)]:
 (R/'data'/f'{name}.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
print('Merged',len(rows),'records,',len(by_offer),'offers and',len(by_url),'sources')
