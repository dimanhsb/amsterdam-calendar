// Regression: manifest fetches must include the same-origin private-site cookie.
// Supply an installed Playwright module and Chromium executable via the variables below.
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {spawn} from 'node:child_process';
import {once} from 'node:events';
import assert from 'node:assert/strict';
const modulePath=process.env.CALENDAR_PLAYWRIGHT_MODULE||'playwright';
const {chromium}=await import(modulePath);
const root=new URL('..',import.meta.url);
const server=spawn('python3',['scripts/qa/auth-server.py'],{cwd:root,stdio:['ignore','pipe','inherit']});
let context;const directory=await fs.mkdtemp(path.join(os.tmpdir(),'calendar-install-'));
try{
 const [chunk]=await once(server.stdout,'data');const base=chunk.toString().trim();
 const options={headless:true,args:['--no-sandbox']};
 if(process.env.CALENDAR_CHROMIUM_EXECUTABLE)options.executablePath=process.env.CALENDAR_CHROMIUM_EXECUTABLE;
 context=await chromium.launchPersistentContext(directory,options);
 const page=await context.newPage();await page.goto(base+'/__test_login');
 await page.waitForFunction(()=>document.querySelector('#weekDate').value.length>0);
 const cdp=await context.newCDPSession(page);
 const manifest=await cdp.send('Page.getAppManifest');
 assert.deepEqual(manifest.errors,[]);assert.equal(JSON.parse(manifest.data).name,'Amsterdam activities');
 const installation=await cdp.send('Page.getInstallabilityErrors');
 assert.deepEqual(installation.installabilityErrors,[],'Chrome must accept a cookie-protected app for installation');
 assert.equal(await page.locator('link[rel="manifest"]').getAttribute('crossorigin'),'use-credentials');
 await page.evaluate(()=>navigator.serviceWorker.ready);
 await page.waitForFunction(()=>!!navigator.serviceWorker.controller);
 // The install event has cached the app shell, icons and data behind the auth gate.
 assert.ok(await page.evaluate(async()=>{const names=await caches.keys();return names.some(n=>n.startsWith('ams-activities-'));}));
 console.log('PASS: Private cookie-protected calendar loads its manifest, icons and service worker; non-incognito Chromium reports zero installation errors.');
}finally{
 await context?.close();server.kill();await fs.rm(directory,{recursive:true,force:true});
}
