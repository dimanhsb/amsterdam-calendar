import {isBlacklisted,DEFAULT_PROFILE} from './preferences.js';
export const TZ = 'Europe/Amsterdam';
export function localDate(value=new Date()){return new Intl.DateTimeFormat('en-CA',{timeZone:TZ,year:'numeric',month:'2-digit',day:'2-digit'}).format(value);}
export function shiftDay(day,n){const d=new Date(day+'T12:00:00Z');d.setUTCDate(d.getUTCDate()+n);return d.toISOString().slice(0,10);}
export function mondayOf(day){const n=new Date(day+'T12:00:00Z').getUTCDay();return shiftDay(day,-((n+6)%7));}
export function nextWeek(today=localDate()){return shiftDay(mondayOf(today),7);}
export function inWeek(e,week){const day=localDate(new Date(e.start));return e.status==='dated'&&day>=week&&day<=shiftDay(week,6);}
export function eligibleForExport(e,profile=DEFAULT_PROFILE){return e.status==='dated'&&e.dateEvidence&&e.start&&!Number.isNaN(Date.parse(e.start))&&!isBlacklisted(e,profile)&&!['cancelled','sold-out','waitlist','conflict'].includes(e.availability);}
export function priceKind(price){if(price.type==='tip-based')return 'tip-based';if(price.type==='donation')return 'donation';if(price.amount===0)return 'free';if(price.amount!=null||price.type==='paid')return 'paid';return 'unknown';}
export function matchesPrice(price,filter='all'){const kind=priceKind(price);if(filter==='all')return true;if(filter==='unknown')return kind==='unknown'||(kind==='paid'&&price.amount==null);if(filter==='paid')return kind==='paid'||(kind==='tip-based'&&price.amount>0);if(['free','donation','tip-based'].includes(filter))return kind===filter;return ['25','50'].includes(filter)&&kind!=='tip-based'&&kind!=='donation'&&price.amount!=null&&price.amount<=Number(filter);}
export function priceLabel(e){const p=e.price,kind=priceKind(p);if(kind==='tip-based')return p.amount>0?'€'+new Intl.NumberFormat('en-GB').format(p.amount)+' + tips':'Tip-based';if(kind==='donation')return 'Donation';if(kind==='free')return 'Free';if(p.amount==null)return p.type==='conflict'?'Price to confirm':kind==='paid'?'Paid · price unknown':'Price unknown';return (p.from?'From ':'')+'€'+new Intl.NumberFormat('en-GB',{minimumFractionDigits:Number.isInteger(p.amount)?0:2,maximumFractionDigits:2}).format(p.amount);}
export function languageCodes(item){return Array.isArray(item.languages)?[...new Set(item.languages.filter(x=>typeof x==='string'&&/^[a-z]{2,3}$/.test(x)))]:[];}
export function languageLabel(item){const codes=languageCodes(item),labels={en:'English',nl:'Dutch',de:'German',fr:'French',es:'Spanish',pap:'Papiamentu',th:'Thai',zxx:'No language needed'};if(!codes.length)return 'Language unconfirmed';const names=codes.map(c=>labels[c]||c.toUpperCase()).join(' / ');return item.languageMode==='multilingual'?(codes.length===1?'Mostly ':'')+names+' · multilingual':names+(item.languageMode==='options'?' options':item.languageMode==='support-staff'?' staff':item.languageSupport?.includes('en')?' · English support':'');}
export function matchesLanguage(item,filter='all'){const codes=languageCodes(item);if(filter==='all')return true;if(filter==='unknown')return !codes.length;if(filter==='other')return codes.some(c=>!['en','nl'].includes(c));return codes.includes(filter);}
export const isWalkingActivity=item=>item.activityType==='walking-tour';
export function safeURL(url){if(!url)return null;try{const u=new URL(url);return ['https:','http:','mailto:'].includes(u.protocol)?u.href:null;}catch{return null;}}
const escapeICS=s=>String(s??'').replace(/\\/g,'\\\\').replace(/\r?\n/g,'\\n').replace(/;/g,'\\;').replace(/,/g,'\\,');
const stamp=t=>new Date(t).toISOString().replace(/[-:]/g,'').replace(/\.\d{3}Z$/,'Z');
function fold(line){let out='',part='',bytes=0;for(const c of line){const b=new TextEncoder().encode(c).length;if(bytes+b>75){out+=part+'\r\n';part=' ';bytes=1;}part+=c;bytes+=b;}return out+part;}
export function makeICS(events,now=new Date(),profile=DEFAULT_PROFILE){
 const lines=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Open Week Amsterdam//EN','CALSCALE:GREGORIAN','METHOD:PUBLISH','X-WR-CALNAME:Open Week Amsterdam'];
 for(const e of events.filter(e=>eligibleForExport(e,profile))){
  lines.push('BEGIN:VEVENT',`UID:${escapeICS(e.id)}@openweek.amsterdam`,`DTSTAMP:${stamp(now)}`,`DTSTART:${stamp(e.start)}`);
  if(e.end)lines.push(`DTEND:${stamp(e.end)}`);
  lines.push(`SUMMARY:${escapeICS(e.title)}`,`LOCATION:${escapeICS(e.address||[e.venue,e.area,'Amsterdam · exact meeting point unconfirmed'].filter(Boolean).join(', '))}`,`DESCRIPTION:${escapeICS(priceLabel(e)+' — '+e.price.note+'\n'+e.description+'\n'+e.attendance+'\nLanguage: '+e.language+'\n'+e.uncertainties.join('\n')+'\nBooking availability unchecked. Saved pick is not a booking. Snapshot checked '+e.checkedAt+'. Recheck organizer for changes.\n'+e.sourceUrls.join('\n'))}`,`URL:${safeURL(e.sourceUrls[0])||''}`,'END:VEVENT');
 }
 lines.push('END:VCALENDAR');return lines.map(fold).join('\r\n')+'\r\n';
}
