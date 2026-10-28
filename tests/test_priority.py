import importlib.util,json,pathlib,subprocess,tempfile,unittest
from unittest.mock import patch
ROOT=pathlib.Path(__file__).resolve().parents[1]

class PriorityTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):cls.data=json.loads((ROOT/'data/source-priority.json').read_text())
 def test_code_queue_precedes_rate_limited_and_has_evidence(self):
  rows=self.data['queues']['deterministic'];self.assertTrue(rows)
  self.assertEqual([x['executionRank'] for x in rows],sorted(x['executionRank'] for x in rows))
  for row in rows:
   if any(x.get('httpStatus')==429 or '429' in x.get('message','') for x in row['lastOutcomes']):
    self.assertIn('Rate limited',row['nextAction']);self.assertIn('do not use a model or browser to evade',row['nextAction'])
 def test_luna_candidates_are_historical_and_do_not_prove_code_failure(self):
  for row in self.data['queues']['luna']:
   self.assertIn(row['audit']['outcome'],('usable','partial'));self.assertIn('spot check',row['evidence']);self.assertIn(row['classification'],('historical_luna_candidate',))
  self.assertIn('code routes may still work',self.data['caveat'])
 def test_blacklisted_domains_do_not_enter_research_queues(self):
  excluded={x['domain'] for x in self.data['queues']['excluded']}
  self.assertIn('beestboulders.com',excluded)
  for name in ('deterministic','code_assessment','luna','harder','unassessed'):
   self.assertFalse(excluded.intersection(x['domain'] for x in self.data['queues'][name]))
 def test_brief_is_code_first_and_uses_curated_entry(self):
  r=subprocess.run(['python3','scripts/source-queue.py','--brief','meetup.com','--start-date','2026-10-28','--end-date','2026-11-02'],cwd=ROOT,capture_output=True,text=True,check=True)
  self.assertIn('deterministic collector',r.stdout);self.assertIn('https://www.meetup.com/find/nl--amsterdam/',r.stdout);self.assertIn('do not book',r.stdout)
 def test_discovery_proposal_is_unverified_and_rejects_secret_url(self):
  spec=importlib.util.spec_from_file_location('guides',ROOT/'scripts/source-guides.py');g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp);(root/'data').mkdir();(root/'research/source-discovery').mkdir(parents=True)
   (root/'data/sources.json').write_text('[]');(root/'data/ideas.json').write_text('[]')
   proposal={'name':'A local maker','discoveryUrl':'https://maker.example/events','organizerOrFeedUrl':'https://secret.example/?token=private','methodObserved':'unassessed','nextStep':'Inspect a public feed.'}
   (root/'research/source-discovery/new.json').write_text(json.dumps({'proposals':[proposal]}))
   with patch.object(g,'ROOT',root):inventory=g.load_sources()
   self.assertIn('maker.example',inventory);self.assertNotIn('secret.example',inventory)
   entry=inventory['maker.example'][0];self.assertIn('unverified',entry['type']);self.assertEqual(entry['discoveryContexts'][0]['nextStep'],'Inspect a public feed.')

if __name__=='__main__':unittest.main()
