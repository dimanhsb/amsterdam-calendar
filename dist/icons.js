// Local, monochrome line icons. Labels remain in text; icons are decorative.
const shapes = {
  dance: '<circle cx="14" cy="4" r="2"/><path d="m5 8 6 2 5-3 4 1M11 10l2 5-5 6m5-6 5 5M11 10l-3 5H4"/>',
  pottery: '<path d="M8 3h8l-1 5c0 2 4 3 4 7 0 3-2 6-7 6s-7-3-7-6c0-4 4-5 4-7L8 3ZM9 8h6M6 15h12M8 19h8"/>',
  art: '<path d="M12 3a9 9 0 1 0 0 18h1a2 2 0 0 0 1-3c-1-1 0-3 2-3h2a3 3 0 0 0 3-3 9 9 0 0 0-9-9Z"/><circle cx="7.5" cy="10" r=".7"/><circle cx="11" cy="6.5" r=".7"/><circle cx="16" cy="8" r=".7"/>',
  needlecraft: '<path d="m5 20 3-7L18 3a2 2 0 0 1 3 3L11 16l-6 4Zm11-13 2-2M5 20c-5-1-2-6 1-4m5 5c4 1 8-2 8-6"/>',
  repair: '<path d="M14 4a6 6 0 0 0-7 7l-4 4a3 3 0 0 0 4 4l4-4a6 6 0 0 0 7-7l-4 3-3-3 3-4Z"/><path d="m6 17 .01.01"/>',
  cooking: '<path d="M8 13H5a3 3 0 0 1-1-6 4 4 0 0 1 6-3 4 4 0 0 1 7 2 3.5 3.5 0 0 1 2 7h-3M8 11v10h8V11M8 17h8"/>',
  coffee: '<path d="M4 9h13v7a5 5 0 0 1-5 5H9a5 5 0 0 1-5-5V9Zm13 1h2a3 3 0 0 1 0 6h-2M7 3v3m5-3v3"/>',
  wine: '<path d="M7 3h10v5a5 5 0 0 1-10 0V3Zm0 5h10m-5 5v8m-4 0h8"/>',
  music: '<path d="M9 18V5l11-2v13M9 9l11-2"/><ellipse cx="6" cy="18" rx="3" ry="2"/><ellipse cx="17" cy="16" rx="3" ry="2"/>',
  theatre: '<path d="m3 4 8 1v7a5 5 0 0 1-8-4V4Zm3 4h1m-1 3 2 1m5-3 8-3v7a6 6 0 0 1-8 6v-4m3-3h1m0 4 2-1"/>',
  writing: '<path d="M13 5H5v16h14v-8M13 5l3-3 4 4-9 9-5 1 1-5 6-6Zm1-1 4 4M5 3h3"/>',
  book: '<path d="M12 6C9 3 5 3 2 4v15c3-1 7-1 10 2 3-3 7-3 10-2V4c-3-1-7-1-10 2Zm0 0v15"/>',
  conversation: '<path d="M21 11a8 8 0 0 1-8 8H8l-5 3 1-6a8 8 0 1 1 17-5Z"/><path d="M8 10h8m-8 4h5"/>',
  games: '<rect x="3" y="3" width="18" height="18" rx="3"/><circle cx="7.5" cy="7.5" r=".7"/><circle cx="16.5" cy="7.5" r=".7"/><circle cx="12" cy="12" r=".7"/><circle cx="7.5" cy="16.5" r=".7"/><circle cx="16.5" cy="16.5" r=".7"/>',
  chess: '<path d="M7 3v5h10V3h-3v3h-4V3H7Zm1 5 1 5-2 5h10l-2-5 1-5M5 18h14v3H5v-3ZM9 13h6"/>',
  walking: '<ellipse cx="8" cy="7" rx="3" ry="5" transform="rotate(-20 8 7)"/><path d="M7 14v3a2 2 0 0 0 4 0v-3"/><ellipse cx="17" cy="14" rx="3" ry="5" transform="rotate(20 17 14)"/><path d="M16 21h3"/>',
  nature: '<path d="M20 3C10 2 3 6 4 13c1 7 12 9 15 0 1-3 1-7 1-10ZM3 21 16 8m-8 8v-5m4 1h5"/>',
  yoga: '<circle cx="12" cy="4" r="2"/><path d="m4 12 4-4 4 2 4-2 4 4M12 10v5m0 0-6 3c-3 1-3 3 1 3h10c4 0 4-2 1-3l-6-3Z"/>',
  fitness: '<path d="m7 7 10 10M3 7l4-4 3 3-4 4-3-3Zm11 11 4-4 3 3-4 4-3-3ZM2 4l2-2m16 20 2-2"/>',
  boxing: '<path d="M7 16c-3-2-4-4-3-7l1-4c1-3 4-2 4 0 0-3 4-3 4 0 1-3 4-2 4 1 3-1 4 1 3 4l-2 6H7Zm1 0v5h9v-5M8 18h9"/>',
  racket: '<ellipse cx="14" cy="9" rx="6" ry="8" transform="rotate(40 14 9)"/><path d="m9 15-6 7m7-15 8 6m-6-9 8 6m-9 1 5-6m-2 9 5-6"/>',
  climbing: '<path d="m2 21 7-14 4 7 3-4 6 11H2Zm4-8 3 1 2-3m5-1 3 6"/><circle cx="15" cy="4" r="2"/>',
  swimming: '<path d="m5 14 5-5 5 5m-5-5-3-4 6-2m-11 15c2-2 3 2 5 0s3 2 5 0 3 2 5 0 3 2 5 0M2 22c2-2 3 2 5 0s3 2 5 0 3 2 5 0 3 2 5 0"/><circle cx="17" cy="8" r="2"/>',
  skating: '<path d="M8 3h7v6l5 4v4H4v-5l4-3V3Zm7 4h-4m4 3h-4M7 17v4m10-4v4M3 21h15c2 0 3-1 3-3"/>',
  rowing: '<path d="M3 14h18l-4 6H7l-4-6Zm-1 8h20M4 3l16 13M3 2l-1 4 4 3 2-3-5-4Z"/>',
  circus: '<circle cx="6" cy="5" r="2"/><circle cx="18" cy="5" r="2"/><circle cx="12" cy="11" r="2"/><path d="m4 12 5 5h6l5-5m-8 5v5m-4 0 4-3 4 3"/>',
  camera: '<path d="M3 7h4l2-3h6l2 3h4v14H3V7Z"/><circle cx="12" cy="14" r="4"/>',
  astronomy: '<path d="m4 7 13-5 3 8-13 5-3-8Zm3 8 3-1m3-1v4m0 0-5 5m5-5 5 5m-5-5v5M2 8l2-1m16-3 2-1"/>',
  lab: '<path d="M8 3h8m-6 0v6L4 19c-1 2 1 2 2 2h12c1 0 3 0 2-2L14 9V3M7 15h10m-7 3h.01m4-1h.01"/>',
  community: '<circle cx="9" cy="7" r="3"/><path d="M3 21v-3a6 6 0 0 1 12 0v3M16 4a3 3 0 0 1 0 6m3 11v-3a6 6 0 0 0-2-4"/>',
};

// Match the activity name first, then its category. Descriptions contain other
// activities and research caveats, so they deliberately do not affect the icon.
const rules = [
  ['camera', /photo|fotograf|fotowandeling|cyanotype|\bfoam\b/i],
  ['astronomy', /astronom|telescope|stargaz|observator|nacht van de nacht/i],
  ['needlecraft', /embroider|sashiko|needlecraft|weav|knit|crochet|naaiatelier|kleding|mending|koekoek|textile/i],
  ['pottery', /pottery|ceramic|clay|klei|wheel.throw|handbuilding|mug workshop/i],
  ['coffee', /barista|coffee workshop/i],
  ['wine', /wine|sommelier/i],
  ['cooking', /cook|cuisine|kook|baking|sourdough|zuurdesem|kimchi|ferment|mezze|tapas|tavola|vis fileren|serve.*(meal|dinner)|food.rescue|surplus.*vegetable/i],
  ['chess', /chess|backgammon/i],
  ['games', /board.?game|bordspell|amsterdice|mahjong|tabletop|role.play|\brpg\b|d&d|pub quiz/i],
  ['racket', /padel|squash|tennis|pétanque/i],
  ['swimming', /swim|aquasport|aquarobic|zuiderbad|mirandabad|noorderparkbad/i],
  ['skating', /skat|ice rink|jaap eden/i],
  ['rowing', /rowing|row & ride|sailing|windsurf|paddl|\bsup\b|kayak|watersport/i],
  ['boxing', /box|muay thai|jiu.jitsu|\bbjj\b|krav maga|boogieland|vos gym|eastbound/i],
  ['climbing', /climb|boulder|klimmuur/i],
  ['circus', /circus|acrobat|aerial|juggling|pole dance|acroyoga/i],
  ['yoga', /yoga|pilates|barre|stretch|flexibility|meditat|breathwork|sound bath|mindful/i],
  ['repair', /repair|reparatie|upcycl|fablab|fabricat|maak het zelf/i],
  ['lab', /wetlab|bio.art|biolog|citizen.science/i],
  ['nature', /garden|terrarium|kokedama|cleanup|clean.up|boterbloem|bird|fungi|autumn trees/i],
  ['walking', /walk|wandel|orienteer|walking.tour/i],
  ['book', /book club|book discussion|reading group|reading|bell jar|storytell|stories|off the page|mythos|pearls on a string|samizdat/i],
  ['writing', /writing|schrijven|kantlijn|bookbind|zine|handletter/i],
  ['theatre', /theat|comedy|improv workshop|improvisatietheater|boom chicago|own sketches/i],
  ['music', /music|muziek|soundlab|sound lab|\bsing(?:ing|along)?\b|choir|karaoke|songwrit|percussion|cajon|conga|bimhuis|orchestre|mezjam|playground jam/i],
  ['dance', /dance|dancing|balfolk|ceilidh|folk|salsa|bachata|merengue|jive|5rhythms|ecstatic|contact.impro|moving dialogues|movement practice|hoopdance|chassé|marthas/i],
  ['conversation', /conversation|discussion|debate|socrates|philosoph|public.speak|just listen|listening|nvc|authentic relating|speedfriend/i],
  ['art', /paint|draw|tekenen|schilder|sketch|art|craft|creati|print|druktechniek|collage|origami|linosnede|linoleum/i],
  ['fitness', /fitness|gym|strength|workout|calisthenic|parkour|saints & stars|kracht/i],
  ['nature', /outdoor/i],
  ['music', /stories|expression/i],
  ['cooking', /food|drink/i],
  ['yoga', /movement/i],
];

export function activityIcon(item) {
  const name = item.title || item.name || '';
  const type = rules.find(([, pattern]) => pattern.test(name))?.[0]
    || rules.find(([, pattern]) => pattern.test(item.category || ''))?.[0]
    || 'community';
  return `<svg class="activity-icon" data-activity-icon="${type}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">${shapes[type]}</svg>`;
}
