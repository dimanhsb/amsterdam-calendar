import {catalogLinks,ideaGroups} from '../catalog.js';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {localDate,nextWeek,mondayOf,inWeek,makeICS,eligibleForExport,priceLabel,priceKind,matchesPrice,languageCodes,languageLabel,matchesLanguage,isWalkingActivity,safeURL} from '../core.js';
import {DEFAULT_PROFILE,isBlacklisted,timeFit,matchesTime,normalizeProfile} from '../preferences.js';
const live=JSON.parse(fs.readFileSync(new URL('../dist/data.json',import.meta.url),'utf8'));
// Historical research assertions use retained canonical records; publication has a rolling cutoff.
const data={...live,events:JSON.parse(fs.readFileSync(new URL('../data/events.json',import.meta.url),'utf8'))};
const cutoff=live.meta.publishedAsOf;
assert.ok(/^\d{4}-\d{2}-\d{2}$/.test(cutoff));
const expected=data.events.filter(e=>!((e.status==='dated'?(e.end||e.start):e.proposedDate)||'')||((e.status==='dated'?(e.end||e.start):e.proposedDate).slice(0,10)>=cutoff));
assert.deepEqual(live.events,expected,'Published payload excludes past records and preserves upcoming records');
assert.equal(live.meta.archivedPastCount,data.events.length-live.events.length);
console.log(`PASS: Rolling publication excludes ${live.meta.archivedPastCount} past records as of ${cutoff}.`);
const baselinePath=new URL('../research/hundred-baseline.json',import.meta.url);
if(fs.existsSync(baselinePath)){
 const baseline=JSON.parse(fs.readFileSync(baselinePath,'utf8')), ids=new Set(baseline.datedIds);
 for(const id of ids)assert.ok(data.events.some(e=>e.id===id),'Retain existing event ID '+id);
 const additional=data.events.filter(e=>eligibleForExport(e)&&!ids.has(e.id));
 assert.ok(additional.length>=baseline.targetAdditionalDated,`At least ${baseline.targetAdditionalDated} new usable dated listings; got ${additional.length}`);
}
const round6BaselinePath=new URL('../research/round6/baseline.json',import.meta.url);
if(fs.existsSync(round6BaselinePath)){
 const baseline=JSON.parse(fs.readFileSync(round6BaselinePath,'utf8')),ids=new Set(baseline.eventIds);
 for(const id of ids)assert.ok(data.events.some(e=>e.id===id),'Round6 preserves existing record '+id);
 const additional=data.events.filter(e=>!ids.has(e.id)&&eligibleForExport(e));
 const preferred=additional.filter(e=>timeFit(e)==='preferred');
 assert.ok(additional.length>=baseline.targetAdditionalDated,`Round6 needs ${baseline.targetAdditionalDated} additional exportable dates; got ${additional.length}`);
 assert.ok(preferred.length>=baseline.targetPreferredDated,`Round6 needs ${baseline.targetPreferredDated} additional preferred-hour dates; got ${preferred.length}`);
 console.log(`PASS: Round6 adds ${additional.length} exportable dates, ${preferred.length} at preferred hours, against the frozen ${baseline.rawDated}-date baseline.`);
}
const unique=(rows,key)=>assert.equal(new Set(rows.map(r=>r[key])).size,rows.length,`Duplicate ${key}`);
const weekendBaselinePath=new URL('../research/round7/baseline.json',import.meta.url);
if(fs.existsSync(weekendBaselinePath)){
 const baseline=JSON.parse(fs.readFileSync(weekendBaselinePath,'utf8')),ids=new Set(baseline.eventIds);
 for(const id of ids)assert.ok(data.events.some(e=>e.id===id),'Weekend research preserves existing record '+id);
 const additional=data.events.filter(e=>!ids.has(e.id)&&eligibleForExport(e)&&baseline.dates.includes(localDate(new Date(e.start))));
 const preferred=additional.filter(e=>timeFit(e)==='preferred');
 assert.ok(additional.length>=baseline.targetAdditionalDated,`Weekend needs ${baseline.targetAdditionalDated} additional exportable dates; got ${additional.length}`);
 assert.ok(preferred.length>=baseline.targetPreferredDated,`Weekend needs ${baseline.targetPreferredDated} additional preferred-hour dates; got ${preferred.length}`);
 console.log(`PASS: Weekend adds ${additional.length} exportable dates, ${preferred.length} at preferred hours, beyond ${baseline.rawWeekend} existing weekend listings.`);
}
for(const rows of [data.events,data.ideas,data.sources,data.offers])unique(rows,'id');
unique(data.sources,'url');
assert.equal(data.ideas.filter(i=>/^seed-\d{3}$/.test(i.id)).length,74,'Preserve original ideas');
for(let i=1;i<=26;i++)assert.ok(data.ideas.some(x=>x.id==='astra-'+String(i).padStart(2,'0')),'Preserve original Astra ideas');
assert.equal(data.meta.coverageStart,'2026-10-19');
assert.ok(data.meta.coverageEnd >= '2026-11-30', 'Coverage retains the original November range');
assert.ok(data.events.some(e=>e.status==='dated'&&e.start.startsWith('2026-11-30')),'Nov30 included');
for(let w='2026-10-19';w<='2026-11-30';){assert.ok(data.events.some(e=>inWeek(e,w)&&eligibleForExport(e)),w+' covered');const t=new Date(w+'T12:00:00Z');t.setUTCDate(t.getUTCDate()+7);w=t.toISOString().slice(0,10);}
const sourceURLs=new Set(data.sources.map(s=>s.url));
for(const e of data.events){
 assert.ok(['dated','lead'].includes(e.status),e.id+' known status');
 assert.ok(['unchecked','available','sold-out','waitlist','cancelled','conflict'].includes(e.availability),e.id+' known availability');
 assert.ok(e.sourceUrls.length&&e.sourceUrls.every(u=>sourceURLs.has(u)),e.id+' source coverage');
 assert.ok(e.sourceUrls.every(safeURL)&&safeURL(e.bookingUrl),e.id+' valid URLs');
 assert.ok(e.checkedAt&&e.venue&&e.area&&e.category&&e.attendance&&e.dateEvidence,e.id+' complete');
 assert.ok(Array.isArray(e.uncertainties));
 assert.ok(Array.isArray(e.sourceUrls),e.id+' source array');
 if(!e.address)assert.ok(e.uncertainties.some(x=>/address|meeting point/i.test(x)),e.id+' unknown location explicit');
 assert.equal(e.price.amount===0,e.price.type==='free',e.id+' unknown is not free');
 assert.ok(e.price.amount==null||(typeof e.price.amount==='number'&&Number.isFinite(e.price.amount)&&e.price.amount>=0));
 if(e.status==='dated'){
  assert.ok(e.start&&/[+-]\d\d:\d\d$/.test(e.start),e.id+' explicit timezone');
  assert.ok(e.start.slice(0,10)>=data.meta.coverageStart&&e.start.slice(0,10)<=data.meta.coverageEnd,e.id+' inside requested range');
  const d=new Date(e.start);assert.ok(Number.isFinite(d.valueOf()));
  assert.equal(localDate(d),e.start.slice(0,10),e.id+' correct Amsterdam local date');
  const localClock=new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Amsterdam',hour:'2-digit',minute:'2-digit'}).format(d);
  assert.equal(localClock,e.start.slice(11,16),e.id+' correct DST offset');
  if(e.end){assert.ok(Date.parse(e.end)>Date.parse(e.start),e.id+' end after start');assert.equal(new Intl.DateTimeFormat('en-GB',{timeZone:'Europe/Amsterdam',hour:'2-digit',minute:'2-digit'}).format(new Date(e.end)),e.end.slice(11,16),e.id+' end Amsterdam offset');}
 }else{assert.equal(e.start,null);assert.equal(eligibleForExport(e),false);}
}
assert.equal(nextWeek('2026-10-18'),'2026-10-19');
assert.equal(nextWeek('2026-10-19'),'2026-10-26');
assert.equal(mondayOf('2026-10-25'),'2026-10-19');
const balfolk=data.events.find(e=>e.id.startsWith('balfolk'));
assert.ok(inWeek(balfolk,'2026-10-19'));
assert.equal(inWeek(balfolk,'2026-10-26'),false);
const ics=makeICS(data.events,new Date('2026-10-18T12:00:00Z'));
assert.ok(ics.includes('DTSTART:20261025T151500Z'),'Sunday CET');
assert.ok(makeICS([{...balfolk,id:'dst-fixture',start:'2026-10-23T19:30:00+02:00',end:'2026-10-23T21:00:00+02:00'}]).includes('DTSTART:20261023T173000Z'),'Friday CEST');
assert.equal((ics.match(/BEGIN:VEVENT/g)||[]).length,data.events.filter(eligibleForExport).length);
assert.ok(!ics.includes('oba-naaiatelier-2026-10-21@'),'No inferred recurrence in export');
assert.ok(!ics.includes('RRULE:'));
for(const e of data.events.filter(e=>e.status==='lead'||['cancelled','sold-out','waitlist','conflict'].includes(e.availability)))assert.ok(!ics.includes('UID:'+e.id+'@'),e.id+' blocked export');
assert.ok(ics.includes('DTSTART:20261130T090000Z'),'Nov30 CET food rescue');
assert.ok(!ics.includes('DTEND:undefined'));
for(const line of ics.split('\r\n'))assert.ok(Buffer.byteLength(line,'utf8')<=75,'ICS byte folding');
assert.equal(safeURL('javascript:alert(1)'),null);
assert.equal(priceLabel({price:{amount:null,type:'unknown'}}),'Price unknown');
assert.equal(priceLabel({price:{amount:null,type:'donation'}}),'Donation');
for(const o of data.offers){
 assert.ok(o.sourceUrls.length&&o.sourceUrls.every(u=>sourceURLs.has(u)&&safeURL(u)),o.id+' offer source coverage');
 assert.ok(safeURL(o.bookingUrl)&&o.scheduleHorizon&&o.checkedAt&&o.venue&&o.attendance,o.id+' offer complete');
 assert.ok(Array.isArray(o.uncertainties)&&o.evidence&&typeof o.evidence==='object'&&!Array.isArray(o.evidence),o.id+' evidence');
 assert.ok(o.directPrice.amount==null||typeof o.directPrice.amount==='number',o.id+' numeric EUR');
 if(o.classpass)assert.ok(safeURL(o.classpass.url)&&o.classpass.creditNote,o.id+' ClassPass limits');
 assert.ok(!o.start&&!ics.includes('UID:'+o.id+'@'),o.id+' undated offer excluded from export');
}
const escapeCase=makeICS([{...balfolk,title:'Comma, semicolon; slash\\ and\nnew line'}]);
assert.ok(escapeCase.includes('SUMMARY:Comma\\, semicolon\\; slash\\\\ and\\nnew line'));
const dup=new Set();for(const e of data.events.filter(eligibleForExport)){const key=[e.title,e.start,e.address].join('|');assert.ok(!dup.has(key),'Duplicate occurrence');dup.add(key);}
for(const file of ['index.html','styles.css','app.js','core.js','icons.js','preferences.js','profile.js','prompts/discover-more.md','prompts/refresh-next-week.md'])assert.ok(fs.existsSync(new URL('../dist/'+file,import.meta.url)));
console.log(`PASS: ${data.events.filter(e=>e.status==='dated').length} dated events, ${data.ideas.length} ideas, ${data.sources.length} sources; DST, export eligibility, URLs and schema checked.`);

assert.deepEqual(data.preferences,DEFAULT_PROFILE,'Built preference defaults match runtime');
const explicitBlacklist=normalizeProfile({blacklist:['climbing','circus-acrobatics']});
for(const title of ['Climbing introduction','Bouldering 101','Aerial silks','AcroYoga jam','Circus & acrobatics','Ground juggling'])assert.ok(isBlacklisted({title,category:''},explicitBlacklist),title+' blacklisted when selected');
for(const title of ['Yoga','Zumba','Samba beginners','Hoopdance workshop','Contact improvisation'])assert.equal(isBlacklisted({title,category:'Dance'},explicitBlacklist),false,title+' allowed');
assert.deepEqual(DEFAULT_PROFILE.blacklist,[],'No activity blacklist by default');
assert.equal(DEFAULT_PROFILE.timeMode,'all','All times shown by default');
assert.equal(matchesTime({start:'2026-10-19T13:00:00+02:00'}),true,'All times available');
const blocked={...balfolk,id:'blacklist-fixture',title:'Bouldering beginner',category:'Climbing'};
assert.equal(eligibleForExport(blocked,explicitBlacklist),false,'Explicit blacklist applies to export');
assert.equal(eligibleForExport(blocked),true,'Default does not blacklist climbing');
const custom=normalizeProfile({customKeywords:['balfolk']});assert.equal(eligibleForExport(balfolk,custom),false,'Custom blacklist applies to export');
assert.ok(data.events.filter(isBlacklisted).every(e=>!ics.includes('UID:'+e.id+'@')),'All blacklisted IDs excluded from export');
console.log('PASS: neutral defaults and explicit blacklist overrides.');

const report=data.report;assert.ok(report,'Research report included');
assert.equal(report.summary.rawDated,data.events.filter(e=>e.status==='dated').length);
assert.equal(report.summary.allowedDated,data.events.filter(e=>e.status==='dated'&&!isBlacklisted(e)).length);
assert.equal(report.summary.preferredDated,data.events.filter(e=>e.status==='dated'&&!isBlacklisted(e)&&timeFit(e)==='preferred').length);
assert.equal(report.summary.exportable,data.events.filter(e=>eligibleForExport(e)).length);
assert.equal(report.ideas.length,data.ideas.length);
assert.equal(report.websites.reduce((sum,w)=>sum+w.primaryEvents,0),report.summary.rawDated);
assert.equal(report.websites.reduce((sum,w)=>sum+w.newEvents,0),report.summary.newDated);
assert.equal(report.rounds.reduce((sum,r)=>sum+r.newDated,0),report.summary.newDated);
for(const w of report.websites)assert.ok(fs.existsSync(new URL('../dist/source-guides/'+w.guide,import.meta.url)),w.domain+' source guide exists');
for(const idea of data.ideas.filter(isBlacklisted)){const row=report.ideas.find(i=>i.id===idea.id);assert.equal(row.events,0);assert.equal(row.offers,0);}
assert.equal(report.ideas.find(i=>i.id==='astra-14').events,0,'Generic repair-cafe index is not bike workshop evidence');
console.log('PASS: generated report matches canonical data, unique primary counts, exclusions, and source guide coverage.');

const audit=data.sourceAudit;assert.ok(audit,'Luna source audit included');
assert.equal(audit.model,'gpt-6-luna');unique(audit.sources,'domain');
assert.equal(audit.summary.websites,audit.sources.length);
assert.equal(audit.summary.liveAttempted+audit.summary.excluded,audit.summary.websites);
assert.equal(audit.summary.usable+audit.summary.partial+audit.summary.blocked+audit.summary.unavailable,audit.summary.liveAttempted);
assert.equal(audit.summary.revisedGuides,audit.sources.filter(s=>s.changed).length);
assert.equal(audit.summary.neededEasierPrompts,audit.sources.filter(s=>s.needsEasierPrompt).length);
for(const source of audit.sources){
 assert.ok(fs.existsSync(new URL('../dist/source-guides/'+source.guide,import.meta.url)),source.domain+' audit guide published');
 if(source.outcome==='excluded')assert.equal(source.attempts.length,0,'Excluded source was guide-only');
 else assert.ok(source.attempts.length&&source.attempts.every(a=>safeURL(a.url)),source.domain+' actual public-page attempts recorded');
}
assert.deepEqual(JSON.parse(fs.readFileSync(new URL('../dist/source-guides/source-audit.json',import.meta.url),'utf8')),audit,'Download matches on-screen audit');
for(const file of ['source-guides/AUDIT.md','prompts/check-one-source.md'])assert.ok(fs.existsSync(new URL('../dist/'+file,import.meta.url)),file+' published');
console.log(`PASS: Luna audit covers ${audit.summary.websites} sources with separate access outcomes, prompt revisions and exclusions.`);

const tips={amount:null,type:'tip-based',from:false};
assert.equal(priceLabel({price:tips}),'Tip-based');assert.equal(matchesPrice(tips,'free'),false);assert.equal(matchesPrice(tips,'tip-based'),true);assert.equal(matchesPrice(tips,'unknown'),false);
assert.equal(matchesPrice({amount:20,type:'paid'},'paid'),true);assert.equal(matchesPrice({amount:0,type:'free'},'free'),true);
assert.equal(matchesLanguage({language:'English website; spoken language not stated',languages:[]},'en'),false);
assert.equal(matchesLanguage({language:'English website; spoken language not stated',languages:[]},'unknown'),true);
assert.equal(matchesLanguage({languages:['nl'],languageSupport:['en']},'en'),false,'Conditional support is not confirmed English delivery');
assert.equal(languageLabel({languages:['en','nl'],languageMode:'options'}),'English / Dutch options');
assert.equal(matchesLanguage({languages:['en','nl'],languageMode:'options'},'nl'),true);
for(const e of [...data.events,...data.offers]){assert.ok(Array.isArray(e.languages),e.id+' structured spoken language');assert.equal(languageCodes(e).length,e.languages.length,e.id+' valid codes');}
assert.ok(data.events.some(e=>isWalkingActivity(e)),'Walking filter has classified walks');
console.log('PASS: free/paid/tip-based distinctions, spoken-language metadata, unknowns and conditional support.');

assert.equal(languageLabel({languages:['en'],languageMode:'multilingual'}),'Mostly English · multilingual');
assert.equal(languageLabel({languages:['en','pap','nl'],languageMode:'multilingual'}),'English / Papiamentu / Dutch · multilingual');
assert.equal(languageLabel({languages:['nl'],languageSupport:['en']}),'Dutch · English support');
assert.equal(languageLabel({languages:['zxx']}),'No language needed');
assert.equal(priceLabel({price:{amount:null,type:'paid'}}),'Paid · price unknown');
assert.equal(matchesPrice({amount:null,type:'paid'},'paid'),true);
assert.equal(matchesPrice({amount:null,type:'paid'},'unknown'),true);

assert.equal(matchesPrice({amount:2,type:'tip-based'},'paid'),true,'Paid admission includes a mandatory reservation fee plus tips');
assert.equal(matchesPrice({amount:2,type:'tip-based'},'25'),false,'Variable tip total is not a guaranteed budget price');

const catalog=data.ideaCatalog;assert.ok(catalog,'Activity/provider catalog included');
for(const rows of [catalog.activities,catalog.providers])unique(rows,'id');
const ideaIds=new Set(data.ideas.map(i=>i.id)),activityIds=new Set(catalog.activities.map(i=>i.id)),providerIds=new Set(catalog.providers.map(i=>i.id));
const associations=new Set();for(const l of catalog.links){assert.ok(ideaIds.has(l.ideaId)&&activityIds.has(l.activityId)&&(l.providerId==null||providerIds.has(l.providerId)),'Catalog references valid');const key=JSON.stringify([l.ideaId,l.activityId,l.providerId]);assert.ok(!associations.has(key),'Catalog relationship unique');associations.add(key);}
for(const id of ideaIds)assert.ok(catalog.links.some(l=>l.ideaId===id),'Preserve every original research note in catalog '+id);
const allSavedURLs=new Set([...data.sources.map(s=>s.url),...data.events.flatMap(e=>e.sourceUrls),...data.offers.flatMap(e=>e.sourceUrls),...data.ideas.flatMap(i=>[i.sourceUrl,...(i.research?.sourceUrls||[])])].filter(Boolean));
for(const p of catalog.providers)assert.ok(!p.url||(safeURL(p.url)&&allSavedURLs.has(p.url)),p.name+' uses saved source URL');
const activeLinks=catalogLinks(data);assert.ok(activeLinks.every(l=>!isBlacklisted(l.idea)&&!isBlacklisted(l.activity)&&(!l.provider||!isBlacklisted(l.provider))),'Blacklist applied at idea, activity and provider level');
assert.equal(catalog.providers.find(p=>p.name==='Studio Klei Amsterdam').url,null,'Unresolved Studio Klei stays separate from Atelier Kleie');
assert.equal(catalog.providers.find(p=>p.name==='FreeDam Tours').url,'https://freedamtours.com/');
assert.equal(ideaGroups(activeLinks,{view:'provider',query:'Common Ground'}).length,1,'Common Ground aliases deduplicated; negative notes do not pollute search');
const pottery=ideaGroups(activeLinks,{query:'Pottery'}).find(a=>a.name==='Pottery & ceramics');assert.ok(pottery.providers.some(p=>p.name.includes('Heart & Soul'))&&pottery.providers.some(p=>p.name==='Atelier Kleie'),'Activity exposes several potential providers');
assert.ok(fs.existsSync(new URL('../dist/catalog.js',import.meta.url)));
console.log('PASS: all research ideas retained, activity/provider references, source URLs, deduplication, blacklist and activity lookup.');
