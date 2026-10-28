import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
groups={
'Creative':[
('CREA','Short workshops, arts, music jams','Course catalog may require a full term; do not assume a five-minute walk.'),
('MK Ateliers / MK24','Drawing, painting, open studio','Verify current identity, open access and individual-session bookings.'),
('Heart & Soul Pottery Studio','Wheel throwing, handbuilding tasters','Check that each workshop is standalone and firing/collection terms.'),
('Art Ceramics Studio · Gillian Smith','Ceramics and glazing','Check current workshop listings and actual address.'),
('The Clay Room Amsterdam','Handbuilding pottery','Verify current studio, format and all-in price.'),
('AGA LAB','Screen printing, etching, risograph','Open lab may require induction or prior technical skills.'),
('Volksuniversiteit Amsterdam','Lectures, photography, writing, conversation','Many offers are courses; look specifically for one-session events.'),
('Amsterdam House of Arts & Crafts','Leather, paint pouring, screen printing, mosaics','Verify public individual bookings; travel claims in pasted text unverified.'),
('De Oude Kerk open studio','Drawing, acoustic jams, architecture sketching','Specific open studio claim unverified; museum access is not a workshop.'),
('Studio Klei Amsterdam','Pottery tasters and decoration','Exact venue, booking model and existence of these sessions need checking.'),
('De Lokatie Upcycling Lab','Textile repair and furniture upcycling','A thrift shop is not evidence of an open workshop; verify lab claim.'),
('Waag Open Wetlab','Bio-art, DIY biology, biomaterials','Historical lab name does not prove current public drop-in access.'),
('Fablab Amsterdam at Waag','Laser cutting, 3D printing, maker nights','Check current operation, inductions and supervised access.'),
('Foam','Photography workshops and walks','Check dates, level and whether exhibition admission is included.')],
'Fitness':[
('Upclub ROW & RIDE','Indoor rowing and cycling','Verify current Weesperstraat venue and pay-per-session access.'),
('Vondelgym Oost','CrossFit, bag training, gymnastics','Single tickets may have experience or membership conditions.'),
('Saints & Stars Oud-Zuid','Boxing, strength, reformer classes','Check location-specific timetable and total single-session cost.'),
('Saints & Stars Oud-West','Bootcamp and strength classes','Check current branch and one-off access.'),
('Het Gymlokaal West','Handstands, mobility, functional movement','Verify beginner entry and one-off ticket.'),
('Kracht Amsterdam','Functional strength and CrossFit','CrossFit visitor drop-in may require prior experience.'),
('Vondelgym West','Kickboxing, running and strength','Distinguish club access from group class entitlement.'),
('Vondelgym Zuid','Functional workouts','Verify class level and independent ticket.'),
('Eastbound Gym','Boxing and Muay Thai','Equipment rental and beginner single-session access need checking.'),
('Tribe Jiu-Jitsu Amsterdam','BJJ fundamentals and open mats','Open mat is often for experienced practitioners; check beginner instruction.'),
('Krav Maga Amsterdam','Self-defense','Exact organizer and one-off beginner policy unverified.'),
('Parkour Discipline Studio','Parkour and freerunning','Exact named venue and adult beginner availability unverified.'),
('Calisthenics Club Amsterdam','Bodyweight classes and handstands','Identify exact organizer; avoid assuming advanced skills are beginner suitable.'),
('Padel Club Metropolitain','Beginner clinics and social play','Check exact club and group-matching rather than court rental alone.'),
('Squash City','Squash and fitness','Court rental requires a playing partner unless a social session is explicit.'),
('Boogieland','Boxing and conditioning','Verify first-timer welcome, equipment and single ticket.'),
('Vos Gym Amsterdam','Kickboxing and bag training','Check current location and beginner class requirements.')],
'Yoga & mindful movement':[
('Svaha Yoga','Yoga and tea afterwards','Social tea and language claims require verification.'),
('Movements City','Hot yoga and Pilates','Check exact address, heat level and single-class terms.'),
('Equal Yoga','Hot yoga and core workouts','Verify beginner level and mat costs.'),
('Studio 191 Amsterdam','Barre, yoga and Pilates','Check branch, equipment and one-off booking.'),
('Yagoy','Yin, restorative yoga and breathwork','Verify current schedule and beginner suitability.'),
('Movements Vondelpark','Hot Pilates and Vinyasa','Check single entry and heat/intensity details.'),
('Sound Bath Amsterdam','Gong and singing-bowl sessions','Identify actual organizer; social contact may be limited.'),
('Wim Hof Method Experience Center','Breathwork and cold exposure','Exact center unverified; do not repeat health benefit claims.'),
('Consciousness Club Amsterdam','Breathwork, meditation and tea','Exact venue/location and current public program unverified.'),
('The Breathwork Movement Studio','Guided breathwork','Verify exact business and format; no medical benefit claims.')],
'Climbing':[
('Klimmuur Amsterdam Centraal','Roped climbing and bouldering','Roped climbing needs training/belay arrangements; day entry is not a social class.'),
('Beest Boulders het Lab Amsterdam','Bouldering','Verify branch naming, entry and shoe hire.'),
('Beest Boulders Amsterdam','Bouldering','Look for coached beginner sessions or hosted social nights.'),
('Beta Boulders Amsterdam','Bouldering and coworking','Check branch/address; pasted Stadionplein claim unverified.'),
('Monk Bouldergym Amsterdam','Bouldering in Noord','Check introductory session and hosted community activities.')],
'Dance':[
('Balfolk at Mezrab / Balfolk Amsterdam','European folk social dance','Priority lead from Greek conversation: introductory workshop, no partner; verify each date.'),
('Dutch traditional folk dance','Dutch regional dances','Curiosity from conversation; distinguish Dutch dances from pan-European Balfolk.'),
('Amsterdam Dance Center','Open ballet, hip-hop, contemporary, jazz, heels','Open class may still require level-specific experience.'),
('Chassé Dance Studios','Afrohouse, street and commercial dance','Check true beginner open classes, not sequential courses.'),
('Lucia Marthas Institute','Musical, pop/show and technique dance','Adult public one-off entry not established by school existence.'),
('Salsa, bachata, merengue beginner socials','Intro plus social dancing','Conditional interest only: must work as a first standalone visit with no partner.'),
('Rock and roll / jive','Social rock dancing','User explicitly declined; retain as excluded, do not recommend.')],
'Circus & acrobatics':[
('Fly Inverted Aerial Studio','Silks, hoop and aerial hammocks','Exact studio and beginner single-session policy unverified.'),
('Pole Dance Factory Amsterdam','Pole, flexibility and chair dance','Check branch, intro prerequisites and independent ticket.'),
('AcroYoga Amsterdam sessions','Partner balance and jams','Jams may require experience; no-partner entry needs explicit confirmation.')],
'Food & drink':[
('De Kookfabriek Amsterdam','Cooking workshops','Private/corporate groups are not public individual bookings.'),
('Amsterdam Wine Academy','Wine tastings and food pairings','Verify exact organizer and single evenings.'),
('Barista Company Academy','Coffee and latte art','Verify exact venue, public booking and equipment inclusions.'),
('Baking Lab Amsterdam','Sourdough, fermentation and circular baking','Check actual public workshop dates and take-home inclusions.')],
'Water & outdoors':[
('Zuiderbad','Swimming and aqua fitness','Lane swimming is lower interaction; classes need separate schedule checks.'),
('De Mirandabad','Swimming and aqua fitness','Separate leisure entry, lap swim and instructed sessions.'),
('Noorderparkbad','Swimming and aquatic classes','Check reservation and ticket type.'),
('Jaap Eden Ice Rink','Ice skating and technique lessons','Seasonal: verify public sessions, rentals and independent beginner lessons.'),
('Canal SUP Amsterdam','SUP tours and SUP yoga','Exact organizer and seasonal schedule unverified.'),
('Sloterpas Watersports Center','Sailing, windsurfing and kayaking','Exact venue name and one-off taught sessions unverified.'),
('Watersportvereniging IJburg','Coastal rowing and paddling','Club membership and beginner safety induction may apply.')],
'Music & expression':[
('Boom Chicago','English improv tasters','Check actual one-off classes rather than course enrollment.'),
("Muziekgebouw aan ’t IJ Sound Lab",'Experimental instruments and sound','Check adult individual tickets; some sessions may be family/group-only.'),
('BIMHUIS Workshop Stage','Jazz and rhythm workshops','Audience masterclasses are not necessarily open playing sessions.'),
('Amsterdam Songwriting Guild','Songwriting feedback circles','Exact organization and public drop-ins unverified.')],
'Talks & writing':[
('Pakhuis de Zwijger','Talks, workshops and civic discussions','Verify language and active participation; a panel audience is lower interaction.'),
('Amsterdam Writing Workshops','Creative writing and feedback','Exact organizer and one-session format unverified.'),
('Debate Club Amsterdam','Debate and public speaking','Exact group near Roeterseiland and guest policy unverified.')]
}
ideas=[]
for cat,rows in groups.items():
 for name,what,note in rows:
  ideas.append(dict(id='seed-%03d'%(len(ideas)+1),name=name,category=cat,description=what,notes=note,status='excluded' if name.startswith('Rock and roll') else 'lead',origin='Conversation' if name.startswith(('Balfolk','Dutch traditional','Salsa','Rock')) else 'Gemini paste',sourceUrl=None))
(ROOT/'data/ideas.json').write_text(json.dumps(ideas,ensure_ascii=False,indent=2)+'\n')
print(f'Preserved {len(ideas)} seed ideas')
