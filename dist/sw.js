// Generated cache identity changes with every build. Only this app's files are cached.
const CACHE = 'ams-activities-87613101d2b0a9d4';
const ASSETS = ["index.html", "styles.css", "app.js", "core.js", "icons.js", "preferences.js", "profile.js", "catalog.js", "data.json", "manifest.webmanifest", "icons/app-192.png", "icons/app-512.png", "icons/amsterdam-calendar.svg", "icons/amsterdam-192.png", "icons/amsterdam-512.png", "icons/amsterdam-32.png", "icons/amsterdam-touch.png", "icons/app.svg", "icons/calendar.svg", "icons/favicon-32.png", "icons/apple-touch-icon.png", "favicon.ico", "prompts/discover-more.md"];
const ROOT = new URL('./', self.location.href);
function cacheable(response){return response.ok && response.type==='basic' && !response.redirected;}
async function checked(response,url){if(!cacheable(response))return false;const type=response.headers.get('content-type')||'';if(url.pathname.endsWith('/')||url.pathname.endsWith('index.html'))return type.includes('text/html')&&(await response.clone().text()).includes('id="eventList"');if(url.pathname.endsWith('.json')||url.pathname.endsWith('.webmanifest'))return /json|manifest/.test(type);if(url.pathname.endsWith('.js'))return /javascript/.test(type);if(url.pathname.endsWith('.css'))return type.includes('text/css');return true;}
self.addEventListener('install',event=>event.waitUntil((async()=>{const cache=await caches.open(CACHE);for(const asset of ASSETS){const url=new URL(asset,ROOT),response=await fetch(url,{cache:'reload'});if(!await checked(response,url))throw Error('App asset unavailable');await cache.put(url,response);}})()));
self.addEventListener('activate',event=>event.waitUntil((async()=>{for(const name of await caches.keys())if(name.startsWith('ams-activities-')&&name!==CACHE)await caches.delete(name);await self.clients.claim();})()));
self.addEventListener('message',event=>{if(event.data?.type==='SKIP_WAITING')self.skipWaiting();});
self.addEventListener('fetch',event=>{
 const url=new URL(event.request.url);if(event.request.method!=='GET'||url.origin!==ROOT.origin)return;
 const navigation=event.request.mode==='navigate'&&(url.pathname===ROOT.pathname||url.pathname===ROOT.pathname+'index.html');
 const key=navigation?new URL('index.html',ROOT).href:url.href;
 if(!navigation&&!ASSETS.some(asset=>new URL(asset,ROOT).href===key))return;
 event.respondWith((async()=>{const cache=await caches.open(CACHE);try{const response=await fetch(event.request);if(await checked(response,url))await cache.put(key,response.clone());return response;}catch(error){const saved=await cache.match(key);if(saved)return saved;throw error;}})());
});
