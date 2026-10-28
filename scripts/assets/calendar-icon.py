"""Render the Amsterdam flag's three crosses on a calendar; no external assets."""
from pathlib import Path
from PIL import Image, ImageDraw
R=Path(__file__).resolve().parents[2]
svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="112" fill="#ed3346"/><rect x="76" y="132" width="360" height="310" rx="36" fill="#b51e32"/><rect x="76" y="112" width="360" height="310" rx="36" fill="#fffaf2"/><path d="M112 112h288a36 36 0 0 1 36 36v54H76v-54a36 36 0 0 1 36-36Z" fill="#b51e32"/><path d="M166 88v54M346 88v54" stroke="#fffaf2" stroke-width="24" stroke-linecap="round"/><path d="M76 236h360v102H76z" fill="#161616"/><path d="m142 263 48 48m-48 0 48-48m66 0 48 48m-48 0 48-48m66 0 48 48m-48 0 48-48" transform="translate(-24)" fill="none" stroke="#fff" stroke-width="16"/><path d="M148 378h34m57 0h34m57 0h34" stroke="#ed3346" stroke-width="14" stroke-linecap="round"/></svg>'''
# Three equally spaced St Andrew's crosses, as on Amsterdam's flag.
svg=svg.replace('m142 263 48 48m-48 0 48-48m66 0 48 48m-48 0 48-48m66 0 48 48m-48 0 48-48','M140 263l48 48m-48 0 48-48M232 263l48 48m-48 0 48-48M324 263l48 48m-48 0 48-48').replace(' transform="translate(-24)"','')
for name in ['app.svg','calendar.svg','amsterdam-calendar.svg']:(R/'icons'/name).write_text(svg+'\n')
scale=4
im=Image.new('RGB',(512*scale,512*scale),'#ed3346');d=ImageDraw.Draw(im)
b=lambda coords:tuple(v*scale for v in coords)
d.rounded_rectangle(b((76,132,436,442)),radius=36*scale,fill='#b51e32')
d.rounded_rectangle(b((76,112,436,422)),radius=36*scale,fill='#fffaf2')
d.rounded_rectangle(b((76,112,436,202)),radius=36*scale,fill='#b51e32');d.rectangle(b((76,157,436,202)),fill='#b51e32')
for x in [166,346]:
 d.line(b((x,88,x,142)),fill='#fffaf2',width=24*scale)
 for y in [88,142]:d.ellipse(b((x-12,y-12,x+12,y+12)),fill='#fffaf2')
d.rectangle(b((76,236,436,338)),fill='#161616')
# Square-ended diagonal bars are polygons, matching SVG stroke geometry.
for x in [164,256,348]:
 for a,c in [((x-24,263),(x+24,311)),((x-24,311),(x+24,263))]:
  dx=c[0]-a[0];dy=c[1]-a[1];length=(dx*dx+dy*dy)**.5;nx=-dy/length*8;ny=dx/length*8
  d.polygon([b((a[0]+nx,a[1]+ny)),b((c[0]+nx,c[1]+ny)),b((c[0]-nx,c[1]-ny)),b((a[0]-nx,a[1]-ny))],fill='#ffffff')
for x in [148,239,330]:
 d.rounded_rectangle(b((x,371,x+34,385)),radius=7*scale,fill='#ed3346')
for size,paths in [(192,['app-192.png','amsterdam-192.png']),(512,['app-512.png','amsterdam-512.png']),(180,['apple-touch-icon.png','amsterdam-touch.png']),(32,['favicon-32.png','amsterdam-32.png'])]:
 for name in paths:im.resize((size,size),Image.Resampling.LANCZOS).save(R/'icons'/name)
im.resize((256,256),Image.Resampling.LANCZOS).save(R/'favicon.ico',format='ICO',sizes=[(16,16),(32,32),(48,48)])
