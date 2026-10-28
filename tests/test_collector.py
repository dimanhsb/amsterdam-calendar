import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('collector',ROOT/'scripts/collect-sources.py')
c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c)

class CollectorTests(unittest.TestCase):
 def test_station_calendar_groups_links_and_keeps_dates_as_leads(self):
  html='''<a href="/platform/msc/conga-2026-10-29/">Conga</a><a href="/platform/msc/conga-2026-10-29/">29 donderdag, 29 okt 20:30 - 21:30 € 23,00 (1 sessie)</a><a href="https://evil.example/platform/msc/other-2026-10-29/">Wrong domain</a><a href="/platform/msc/invalid-2026-99-99/">Bad date</a>'''
  rows=c.parse_station(html,'https://station-west.amsterdam/msc/','2026-10-28','2026-11-30')
  self.assertEqual(len(rows),1);self.assertEqual(rows[0]['title'],'Conga');self.assertEqual(rows[0]['date'],'2026-10-29');self.assertEqual(rows[0]['startTime'],'20:30');self.assertEqual(rows[0]['priceText'],'€ 23,00');self.assertTrue(rows[0]['needsReview'])
  self.assertNotIn('status',rows[0])
 def test_oba_link_discovery_never_invents_an_event_date(self):
  html='<a href="/nl/agenda/volledige-agenda">Index</a><a href="/nl/agenda/art-workshop">Art workshop</a><a href="/nl/agenda/art-workshop">Duplicate</a><a href="https://elsewhere.example/nl/agenda/other">Other</a>'
  rows=c.parse_oba(html,'https://oba.nl/nl/agenda/volledige-agenda','2026-10-28','2026-11-30')
  self.assertEqual(len(rows),1);self.assertEqual(rows[0]['title'],'Art workshop');self.assertIsNone(rows[0]['eventDate']);self.assertTrue(rows[0]['needsReview'])
 def test_pakhuis_card_and_wijkconnect_slide_are_only_leads(self):
  pakhuis='<div class="program teaser"><a href="/programma/night" class="program-link"></a><div class="details"><div class="title truncate">A workshop</div><div class="meta"><div class="date-time">Vandaag, 19.00</div></div></div></div>'
  rows=c.parse_pakhuis(pakhuis,'https://dezwijger.nl/agenda','2026-10-28','2026-11-30')
  self.assertEqual(rows[0]['title'],'A workshop');self.assertEqual(rows[0]['scheduleText'],'Vandaag, 19.00');self.assertIsNone(rows[0]['eventDate'])
  slide='<div class="slide"><div class="content"><h1>Disco</h1><span class="event_recurrence">Friday weekly</span><div><script>var x = {text: "https://www.wijkconnect.com/amsterdam/organisaties/8345/huis-van-de-buurt-de-boomsspijker/agenda/123/disco"}</script></div></div></div>'
  rows=c.parse_wijkconnect(slide,'https://www.wijkconnect.com/amsterdam/organisaties/8345/huis-van-de-buurt-de-boomsspijker/agenda_items/slides','2026-10-28','2026-11-30')
  self.assertEqual(rows[0]['title'],'Disco');self.assertEqual(rows[0]['scheduleText'],'Friday weekly');self.assertIsNone(rows[0]['eventDate'])
 def test_server_rate_limit_has_conservative_backoff(self):
  from urllib.error import HTTPError
  e=HTTPError('https://example.org/robots.txt',429,'Too many requests',{'Retry-After':'600'},None)
  self.assertEqual(c.retry_after_seconds(e),600)
 def test_article_publication_is_not_event_date(self):
  html='''<article><header><h1 class="entry-title"><a href="/fan/">Fan club</a></h1><time class="entry-date" datetime="2026-10-22T10:00:00+02:00">22 Oct</time></header><div class="entry-content"><p>Meets 2 November.</p></div></article>'''
  rows=c.parse_articles(html,'https://example.org/category/activities/','2026-10-28','2026-11-30')
  self.assertEqual(rows[0]['publishedAt'][:10],'2026-10-22');self.assertIsNone(rows[0]['eventDate']);self.assertIsNone(rows[0]['inWindow']);self.assertIn('2 November',rows[0]['excerpt'])
 def test_repeated_wildcard_robots_groups_are_all_respected(self):
  robots='User-agent: *\nDisallow: /admin/\n\nUser-agent: *\nDisallow: /private/\nCrawl-delay: 60\n'
  self.assertFalse(c.robots_can_fetch(robots,'https://example.org/private/a'));self.assertTrue(c.robots_can_fetch(robots,'https://example.org/events/'));self.assertEqual(c.wildcard_delay(robots),60)
 def test_reparse_rejects_path_traversal_source_id(self):
  with tempfile.TemporaryDirectory() as tmp:
   source={'id':'../bad','name':'Bad','url':'https://example.org/','adapter':'wordpress_articles'}
   with patch.object(c,'CACHE',Path(tmp)),patch.object(c,'fetch') as fetch:
    result=c.reparse(source,'2026-10-28','2026-11-30',Path(tmp),'20261028T083025097604Z')
   self.assertEqual(result['outcome'],'configuration_error');fetch.assert_not_called()
 def test_reparse_uses_saved_html_without_network_and_preserves_fetch_time(self):
  import hashlib,json
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);old='20261028T083025097604Z';old_dir=root/'runs'/old;old_dir.mkdir(parents=True)
   html=b'<div class="program teaser"><a class="program-link" href="/programma/a"></a><div class="title">An event</div></div>'
   (old_dir/'pdz.html').write_bytes(html);source={'id':'pdz','name':'Pakhuis','url':'https://dezwijger.nl/agenda','adapter':'pakhuis_agenda_links'}
   (old_dir/'run.json').write_text(json.dumps({'results':[{'sourceId':'pdz','sourceUrl':source['url'],'cacheKey':f'runs/{old}/pdz.html','sha256':hashlib.sha256(html).hexdigest(),'httpStatus':200,'startedAt':'2026-10-28T08:30:25+00:00'}]}))
   new_dir=root/'new';new_dir.mkdir()
   with patch.object(c,'CACHE',root),patch.object(c,'fetch') as fetch:
    result=c.reparse(source,'2026-10-28','2026-11-30',new_dir,old)
   fetch.assert_not_called();self.assertEqual(result['outcome'],'success');self.assertEqual(result['sourceFetchedAt'],'2026-10-28T08:30:25+00:00');self.assertEqual(result['candidateCount'],1)
 def test_long_robots_delay_defers_page_fetch(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=Path(tmp);state={};source={'id':'example','name':'Example','url':'https://example.org/events/','adapter':'wordpress_articles','minDelaySeconds':1}
   robots=b'User-agent: *\nAllow: /\nCrawl-delay: 60\n'
   with patch.object(c,'CACHE',root),patch.object(c,'fetch',return_value=(200,'https://example.org/robots.txt','text/plain',robots)) as fetch:
    result=c.collect(source,'2026-10-28','2026-11-30',root,state)
   self.assertEqual(result['outcome'],'deferred_rate_limit');self.assertEqual(fetch.call_count,1);self.assertIsNone(result['cacheKey'])

if __name__=='__main__':unittest.main()
