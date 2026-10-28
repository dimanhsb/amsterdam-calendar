"""Initial source import. Preserve raw snapshots; canonical records are independently editable."""
import json,pathlib,re,copy
R=pathlib.Path(__file__).resolve().parents[1]
load=lambda p:json.loads((R/p).read_text())
source_by_url={}
for fn in ['dance-social.json','creative-active.json']:
 for s in load('research/'+fn)['sources']:
  u=s['url'];source_by_url[u]={'id':'source-%03d'%(len(source_by_url)+1),'title':s.get('title') or s.get('id','').replace('-',' ').title() or u.split('/')[2],'url':u,'type':s.get('type','Research source'),'evidence':s.get('evidence',''),'checkedAt':s.get('checkedAt','2026-10-18')}
events=[]
formats={
'balfolk':('Dance','Eastern Docklands','active','Dance together','Partner and group changes give you a natural way to join in.','Ticket required; no fixed partner or prior dance experience needed.','Mezrab'),
'dance-playground':('Dance','Oud-West','active','Movement exploration','Guided movement tools, then space to move alone or connect.','One 90-minute ticketed session. English and Dutch listed.','OT301'),
'mezrab-open-stage':('Stories & improv','Eastern Docklands','audience','Audience / optional story','Listen to stories, or ask about a first-timer performance slot.','One evening; audience can attend without performing.','Mezrab'),
'mezrab-friday':('Stories & improv','Eastern Docklands','audience','Mostly audience','A relaxed outing, with conversation possible around a seated show.','Standalone evening. Confirm price and language.','Mezrab'),
'adev':('Dance','Noord','unknown','Format to confirm','A public dance event; the actual participation format needs checking.','Free listing; beginner and partner requirements not stated.','De Ceuvel'),
'playground-jam':('Music & movement','Oost','active','Make something together','Movers and musicians improvise together after a guided warm-up.','First-timers welcome; English; minimum €10 sliding scale.','Common Ground'),
'city-walk':('Outdoors','Centrum','group','Walk & talk','A shared route and leisurely pace leave space for conversation.','Join independently; walking shoes recommended; 8 km listing.','Amsterdam Centraal · city side'),
'serve-city':('Volunteering','Nieuw-West','active','Shared task','Work alongside other volunteers while walking through the park.','Registration required; must live in the Netherlands. Meeting point follows signup.','Sloterpark'),
'easylaughs':('Stories & improv','Oost / Roeterseiland','active','Group improv','Group exercises create interaction; beginner level is not stated.','One ticketed workshop; English. Check prior experience requirements.','CREA'),
'pink-dance':('Dance','Oud-West','active','Social dance · specific audience','Social dance for LGBTQ+ people aged 50+ and friends; fit is not assumed.','€5 cash, drinks extra. Intended for LGBTQ+ 50+ community and friends.','Het Open Huis'),
'oba-origami':('Creative','De Pijp / CC Amstel','group','Small-group making','Learn folds together in a beginner workshop with a shared focus.','Ages 16+; email registration required. Fee not stated.','OBA CC Amstel'),
'ahac':('Creative','Centrum / Oudeschans','group','Small-group making','A shared studio and guided projects give you something to talk about.','One two-hour booking; no experience needed; supplies included.','House of Arts & Crafts'),
'boulder':('Climbing','Zuid / Schinkel','active','Beginner group','Start alongside other beginners with instruction and time to climb.','One-off 90-minute introduction; 14+; confirm promotional total.','Boulderhal Luchthaven'),
'atelier-kleie':('Creative','Nieuw-West','group','Small-group making','Work with clay in a guided session; conversation depends on the group.','Explicit single-session booking; materials, firing and glazing listed.','Atelier Kleie'),
'oba-naai':('Creative','De Pijp / CC Amstel','group','Open making · confirm date','A supported sewing space with a personal project to work on.','Weekly schedule only; bring a project and verify this week.','OBA CC Amstel'),
'repair-cafe':('Creative','De Pijp','unknown','Repair help · confirm date','A repair clinic may offer conversation, but it is not necessarily a class.','Date needs rechecking because venue profile has stale information.','Repair Café De Pijp')}
for fn in ['dance-social.json','creative-active.json']:
 for raw in load('research/'+fn)['events']:
  key=next((k for k in formats if raw['id'].startswith(k)),None)
  if not key:raise Exception(raw['id'])
  cat,area,part,fl,social,att,venue=formats[key]
  amount=raw.get('price',{}).get('amount_eur',raw.get('priceEUR'))
  pn=raw.get('price',{}).get('note',raw.get('priceEvidence','Price not stated.'))
  ev=raw.get('evidence',{}) or {k:raw[v] for k,v in [('beginner','beginnerEvidence'),('single_session','singleSessionEvidence'),('reservation','reservationEvidence')] if v in raw}
  urls=raw.get('source_urls',raw.get('sourceURLs',[]))
  status='dated' if raw['status']=='dated-confirmed' and key!='repair-cafe' else 'lead'
  e={'id':raw['id'],'title':raw['title'],'status':status,'start':raw['start'] if status=='dated' else None,'end':raw.get('end') if status=='dated' else None,'proposedDate':raw['start'][:10] if status!='dated' else None,'timezone':'Europe/Amsterdam','category':cat,'area':area,'venue':raw.get('venue',venue),'address':raw['address'],'description':raw['title'].split(' (')[0]+'. '+att,'participation':part,'formatLabel':fl,'socialReason':social+' (Editorial assessment.)','attendance':att,'language':ev.get('language',raw.get('language','Not stated.')),'bookingUrl':raw.get('booking_url',raw.get('bookingURL')),'sourceUrls':urls,'dateEvidence':'Organizer dated listing' if status=='dated' else 'Date needs confirmation','evidence':ev,'checkedAt':raw.get('checkedAt','2026-10-18'),'uncertainties':raw.get('uncertainties',[]),'availability':'unchecked','price':{'amount':amount,'type':'free' if amount==0 else 'paid' if amount is not None else 'unknown','from':key=='playground-jam','note':pn,'caption':'Verify fees / checkout' if amount is not None else 'Ask organizer / see details'}}
  if key=='dance-playground':e['price']['type']='conflict'
  if key=='ahac':
   e['dateEvidence']='Dated city listing + organizer' if status=='dated' else 'Exact date not independently observed'
   e['language']='Delivery language not explicitly confirmed; English information is available.'
   if 'clay-sculpting' in e['id']:e['title']='Clay & sculpting · Open Studio';e['description']='A standalone clay-making session within Open Studio. No experience required; some pieces need later collection.';e['price']['from']=True
  if key=='balfolk':e['arrival']='Doors 16:15 · beginner workshop 16:30';e['price']['caption']='€18.50 advance · €20 door';e['uncertainties'].append('October uses the fourth Sunday, an explicit exception to the usual third Sunday. Instruction language is unstated.');e['sourceUrls'].append('https://balfolkamsterdam.nl/bal')
  if key=='oba-origami':e['uncertainties'].append('Listing gives a 17:30–19:00 window but describes 75 minutes of instruction; confirm when instruction begins.')
  if key=='boulder':e['uncertainties'].append('Organizer states cancellation is free until seven days before; after that no refund or rescheduling.');e['price']['caption']='Promo incl. lesson & shoes';e['language']='Trainers teach Dutch and English; confirm this particular session if essential.'
  if key in ['mezrab-open-stage','mezrab-friday']:e['sourceUrls'].append('https://mezrab.nl/full-program/');e['end']=None;e['uncertainties'].append('End time omitted here because the exact date is confirmed separately from generic session hours.')
  if key=='playground-jam':e['uncertainties']=['Ticket inventory and instrument borrowing arrangements have not been checked.']
  events.append(e)
u='https://www.ivn.nl/afdeling/amsterdam/natuuractiviteiten/herfstwandeling-in-het-beatrixpark-bijzondere-en-zeldzame-bomen-zaden-en-vruchten-2/'
events.append({'id':'ivn-beatrixpark-2026-10-25','title':'Autumn trees, seeds & fruits walk','status':'dated','start':'2026-10-25T13:00:00+01:00','end':'2026-10-25T14:30:00+01:00','proposedDate':None,'timezone':'Europe/Amsterdam','category':'Outdoors','area':'Zuid / Beatrixpark','venue':'Beatrixpark · Diepenbrockstraat','address':'Beatrixpark – Diepenbrockstraat, 1077 VX Amsterdam','description':'A guided autumn walk exploring unusual trees, fruits and seeds. Adult activity, maximum 12 participants.','participation':'group','formatLabel':'Small guided group','socialReason':'A small shared walk offers prompts for conversation. (Editorial assessment.)','attendance':'Mandatory email registration; maximum 12 participants; adult activity.','language':'Not stated; organizer page is in Dutch.','bookingUrl':'mailto:WandelingBeatrixpark@outlook.com','sourceUrls':[u],'dateEvidence':'Organizer dated listing','evidence':{'date':'Organizer explicitly lists 25 October 2026, 13:00–14:30.','registration':'Free; email registration mandatory, maximum 12 participants.'},'checkedAt':'2026-10-18','uncertainties':['Remaining places, delivery language and weather changes not checked. Confirm the precise park entrance in registration.'],'availability':'unchecked','price':{'amount':0,'type':'free','from':False,'note':'Organizer explicitly lists free participation. Registration required.','caption':'Registration required'}})
source_by_url[u]={'id':'source-ivn-beatrixpark','title':'IVN · Beatrixpark autumn walk · 25 October','url':u,'type':'Organizer event page','checkedAt':'2026-10-18','evidence':'Exact date and hours, free admission, registration by email, adult outing, maximum 12, park meeting location.'}
for e in events:
 for u in e['sourceUrls']:
  if u not in source_by_url:source_by_url[u]={'id':'source-%03d'%(len(source_by_url)+1),'title':u.split('/')[2]+' · '+u.rstrip('/').split('/')[-1].replace('-',' '),'url':u,'type':'Supporting organizer page','checkedAt':'2026-10-18','evidence':'Supporting link retained with the event. See event evidence and uncertainty notes.'}
# Parse Astra's complete table, retaining hypotheses as hypotheses.
ideas=load('data/ideas.json');ideas=[i for i in ideas if i['origin']!='Astra']
for line in (R/'research/astra-ideas-review.md').read_text().splitlines():
 if not re.match(r'\| \d+ \|',line):continue
 cols=[c.strip() for c in line.strip('|').split('|')];n,name,why,note=cols
 urls=re.findall(r'\]\((https?://[^)]+)\)',note)
 clean=re.sub(r'\[([^\]]+)\]\([^)]+\)',r'\1',note)
 ideas.append({'id':'astra-%02d'%int(n),'name':name,'category':'New directions','description':why,'notes':clean,'status':'lead','origin':'Astra','sourceUrl':urls[0] if urls else None})
# Editorial titles retain full original wording in raw research files.
for e in events:
 if e['id'].startswith('ahac') and e['status']=='lead':e['title']='Open Atelier · choose your craft'
 if e['id'].startswith('boulder'):e['title']='Bouldering 101 · beginner introduction'
 if e['id'].startswith('atelier-kleie'):e['title']='Pottery · hand-building introduction'
 if e['id'].startswith('balfolk'):e['title']='Balfolk social · live music & beginner workshop'
 if e['id'].startswith('serve-city'):e['venue']='Sloterpark · meeting point after signup'
for s in source_by_url.values():
 if 'meetup.com' in s['url']:s['type']='Unverified discovery result';s['evidence']='Meetup event and group pages failed to open. Search text is retained only as a research lead; dates, price and attendance details remain unverified.'
 if 'andreas.amsterdam' in s['url']:s['type']='Aggregator / discovery source';s['evidence']='Secondary discovery listing; exact event claims rely on the venue link retained with the event.'
 if 'wednesdays' in s['url']:s['evidence']='General Wednesday format: audience attendance and first-time/spontaneous storytelling. Exact 21 October start is corroborated by the full program; the category page does not establish an occurrence-specific end.'
 if 'fridays' in s['url']:s['evidence']='General Friday storytelling format. Exact 23 October start is corroborated by the full program; generic session hours are not treated as an occurrence-specific end.'
for key,value in [('events',events),('sources',list(source_by_url.values())),('ideas',ideas)]:
 (R/'data'/f'{key}.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')
print(f'Curated {sum(e["status"]=="dated" for e in events)} dated events and {sum(e["status"]=="lead" for e in events)} schedule leads; {len(ideas)} ideas; {len(source_by_url)} sources')
