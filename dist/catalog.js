import {isBlacklisted,DEFAULT_PROFILE} from './preferences.js';

export function catalogLinks(data,profile=DEFAULT_PROFILE){
 const catalog=data.ideaCatalog||{},ideas=new Map(data.ideas.map(i=>[i.id,i])),activities=new Map((catalog.activities||[]).map(a=>[a.id,a])),providers=new Map((catalog.providers||[]).map(p=>[p.id,p]));
 const links=[],seen=new Set(),mapped=new Set();
 for(const entry of catalog.links||[]){
  const idea=ideas.get(entry.ideaId),activity=activities.get(entry.activityId),provider=entry.providerId?providers.get(entry.providerId):null;
  if(!idea||!activity||(entry.providerId&&!provider))continue;
  mapped.add(idea.id);
  if(isBlacklisted(idea,profile)||isBlacklisted(activity,profile)||(provider&&isBlacklisted(provider,profile)))continue;
  const key=JSON.stringify([idea.id,activity.id,provider?.id||null]);if(seen.has(key))continue;seen.add(key);links.push({idea,activity,provider});
 }
 // New research stays visible even before its activity/provider classification is curated.
 for(const idea of data.ideas)if(!mapped.has(idea.id)&&!isBlacklisted(idea,profile))links.push({idea,activity:{id:'unclassified',name:'Ideas to classify',category:'Research',description:'New research awaiting activity and provider classification.'},provider:null});
 return links;
}
const unique=(rows,key)=>[...new Map(rows.map(row=>[row[key],row])).values()];
export function ideaGroups(links,{view='activity',category='all',query='',selection=null}={}){
 const q=query.trim().toLocaleLowerCase(),groups=new Map();
 for(const row of links){
  if(category!=='all'&&row.activity.category!==category)continue;
  const entity=view==='provider'?row.provider||{id:'provider-needed',name:'Provider not yet identified',notes:'These activities still need a potential provider.'}:row.activity;
  if(selection&&entity.id!==selection)continue;
  const text=[row.activity.name,row.activity.category,row.provider?.name,...(row.provider?.aliases||[]),row.idea.name].join(' ').toLocaleLowerCase();
  if(q&&!text.includes(q))continue;
  if(!groups.has(entity.id))groups.set(entity.id,{...entity,links:[]});groups.get(entity.id).links.push(row);
 }
 return [...groups.values()].map(g=>({...g,ideas:unique(g.links.map(r=>r.idea),'id'),activities:unique(g.links.map(r=>r.activity),'id'),providers:unique(g.links.flatMap(r=>r.provider?[r.provider]:[]),'id')})).sort((a,b)=>(a.id==='provider-needed')-(b.id==='provider-needed')||a.name.localeCompare(b.name));
}
