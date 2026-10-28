import {DEFAULT_PROFILE} from './profile.js';
export {DEFAULT_PROFILE};
export const BLACKLIST_RULES = [
  {id:'climbing',label:'Climbing & bouldering',pattern:/\b(?:climb(?:ing)?|boulder(?:ing|s)?|bouldergym|klimmuur)\b/i},
  {id:'circus-acrobatics',label:'Circus & acrobatics',pattern:/\b(?:circus|acrobat(?:ic|ics)?|acro.?yoga|aerial|pole(?: dance| fitness)?|juggling|handstand|object.manipulation)\b/i},
];
export function normalizeProfile(value={}) {
  if(!value||typeof value!=='object'||Array.isArray(value)) value={};
  return {...DEFAULT_PROFILE,...value,
    blacklist:Array.isArray(value.blacklist)?value.blacklist.filter(id=>BLACKLIST_RULES.some(r=>r.id===id)):[...DEFAULT_PROFILE.blacklist],
    customKeywords:Array.isArray(value.customKeywords)?[...new Set(value.customKeywords.filter(s=>typeof s==='string').map(s=>s.trim()).filter(Boolean))]:[],
    timeMode:['all','preferred'].includes(value.timeMode)?value.timeMode:DEFAULT_PROFILE.timeMode,
    weekdayEveningStart:DEFAULT_PROFILE.weekdayEveningStart,
    weekdayMorningEnd:DEFAULT_PROFILE.weekdayMorningEnd,
    timezone:DEFAULT_PROFILE.timezone,
  };
}
export function blacklistReason(item,profile=DEFAULT_PROFILE) {
  profile=normalizeProfile(profile);
  if(item.status==='excluded')return 'Previously declined';
  const text=[item.title||item.name||'',item.category||''].join(' ');
  const rule=BLACKLIST_RULES.find(r=>profile.blacklist.includes(r.id)&&r.pattern.test(text));
  if(rule)return rule.label;
  const keyword=profile.customKeywords.find(k=>text.toLocaleLowerCase().includes(k.toLocaleLowerCase()));
  return keyword?`Keyword: ${keyword}`:null;
}
export const isBlacklisted=(item,profile=DEFAULT_PROFILE)=>Boolean(blacklistReason(item,profile));
export function timeFit(item,profile=DEFAULT_PROFILE) {
  profile=normalizeProfile(profile);
  if(!item.start||Number.isNaN(Date.parse(item.start)))return 'unknown';
  const parts=t=>Object.fromEntries(new Intl.DateTimeFormat('en-CA',{timeZone:profile.timezone,year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',minute:'2-digit',hourCycle:'h23'}).formatToParts(new Date(t)).map(p=>[p.type,p.value]));
  const start=parts(item.start),day=`${start.year}-${start.month}-${start.day}`;
  const weekday=new Date(day+'T12:00:00Z').getUTCDay(),clock=`${start.hour}:${start.minute}`;
  if(profile.weekends&&(weekday===0||weekday===6))return 'preferred';
  if(clock>=profile.weekdayEveningStart)return 'preferred';
  if(clock<profile.weekdayMorningEnd) {
    if(!item.end||Number.isNaN(Date.parse(item.end)))return 'unknown';
    const end=parts(item.end),endDay=`${end.year}-${end.month}-${end.day}`;
    return endDay===day&&`${end.hour}:${end.minute}`<=profile.weekdayMorningEnd&&Date.parse(item.end)>Date.parse(item.start)?'preferred':'outside';
  }
  return 'outside';
}
export const matchesTime=(item,profile=DEFAULT_PROFILE)=>normalizeProfile(profile).timeMode==='all'||timeFit(item,profile)==='preferred';
