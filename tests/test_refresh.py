import importlib.util, json, pathlib, tempfile, unittest
from unittest.mock import patch

P=pathlib.Path(__file__).resolve().parents[1]/'scripts/refresh.py'
spec=importlib.util.spec_from_file_location('refresh',P); refresh=importlib.util.module_from_spec(spec); spec.loader.exec_module(refresh)

class RefreshTest(unittest.TestCase):
 def test_partial_preview_preserves_events_and_caps_queue(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp); (root/'data').mkdir(); (root/'scripts').mkdir()
   runs=root/'data/collection-runs.json'; reports=root/'data/refresh-runs.json'; cache=root/'.collector-cache'
   (root/'data/events.json').write_text('[{"id":"saved"}]')
   def collect(*args, **kwargs):
    run={'id':'run1','startedAt':'2026-10-28T00:00:00Z','results':[{'sourceId':'ok','name':'OK','outcome':'success','candidateCount':2,'candidates':[{'url':'https://example.org/a'},{'url':'https://example.org/b'}]},{'sourceId':'failed','name':'Failed','outcome':'fetch_error','candidateCount':0,'message':'timeout'}]}
    runs.write_text(json.dumps([run])); return type('P',(),{'returncode':1})()
   with patch.multiple(refresh, ROOT=root,CACHE=cache,RUNS=runs,REPORTS=reports), patch.object(refresh.subprocess,'run',side_effect=collect), patch('sys.argv',['refresh.py','--preview','--luna-limit','1']):
    self.assertEqual(refresh.main(),1)
   report=json.loads(reports.read_text())[0]; queue=json.loads((cache/'runs/run1/model-queue.json').read_text())
   self.assertEqual(report['outcome'],'partial');self.assertEqual(report['luna']['status'],'unavailable')
   self.assertEqual(len(queue['items']),1);self.assertEqual(queue['skippedByLimit'],1)
   self.assertEqual(json.loads((root/'data/events.json').read_text()),[{'id':'saved'}])
 def test_bad_date_rejected_without_creating_files(self):
  with tempfile.TemporaryDirectory() as tmp:
   root=pathlib.Path(tmp)
   with patch.multiple(refresh,ROOT=root,CACHE=root/'cache',RUNS=root/'runs',REPORTS=root/'reports'),patch('sys.argv',['refresh.py','--start-date','2026-11-02','--end-date','2026-11-01']):
    with self.assertRaises(SystemExit): refresh.main()
   self.assertEqual(list(root.iterdir()),[])
if __name__=='__main__':unittest.main()
