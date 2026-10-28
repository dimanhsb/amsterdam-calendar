#!/usr/bin/env python3
"""Run an on-demand source collection and record what remains to be reviewed."""
import argparse, datetime as dt, fcntl, json, subprocess, sys
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / '.collector-cache'
RUNS = ROOT / 'data/collection-runs.json'
REPORTS = ROOT / 'data/refresh-runs.json'
TZ = ZoneInfo('Europe/Amsterdam')

def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')

def read(path, default):
    return json.loads(path.read_text(encoding='utf-8')) if path.exists() else default

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + '.tmp')
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    tmp.replace(path)

def main():
    today = dt.datetime.now(TZ).date()
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--start-date', default=today.isoformat())
    p.add_argument('--end-date', default=(today + dt.timedelta(days=27)).isoformat())
    p.add_argument('--source', action='append', help='Only collect this configured source; may be repeated')
    p.add_argument('--preview', action='store_true', help='Collect and write local reports, but do not build the site')
    p.add_argument('--luna-limit', type=int, default=20)
    p.add_argument('--terra-limit', type=int, default=2)
    a = p.parse_args()
    try:
        start, end = dt.date.fromisoformat(a.start_date), dt.date.fromisoformat(a.end_date)
        if start > end or a.luna_limit < 0 or a.terra_limit < 0: raise ValueError()
    except ValueError:
        p.error('Use an ordered ISO date range and non-negative model limits')
    CACHE.mkdir(parents=True, exist_ok=True)
    with (CACHE / 'refresh.lock').open('a') as lock:
        try: fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            print('Another refresh is active; no changes made.', file=sys.stderr); return 2
        before = {r['id'] for r in read(RUNS, [])}
        command = [sys.executable, str(ROOT/'scripts/collect-sources.py'), '--start-date', str(start), '--end-date', str(end)]
        for source in a.source or []: command.extend(['--source', source])
        proc = subprocess.run(command, cwd=ROOT)
        new_runs = [r for r in read(RUNS, []) if r['id'] not in before]
        if len(new_runs) != 1:
            print('Collector did not produce a run; no refresh was recorded.', file=sys.stderr); return 1
        collected = new_runs[0]
        results = collected.get('results', [])
        # These are leads only: no model-backed or verified extraction is available here.
        leads = [(s, c) for s in results if s.get('outcome') == 'success' for c in s.get('candidates', []) if c.get('inWindow') is not False]
        queued = leads[:a.luna_limit]
        run_dir = CACHE/'runs'/collected['id']
        write(run_dir/'model-queue.json', {'windowStart':str(start), 'windowEnd':str(end), 'items':[{'sourceId':s['sourceId'], 'candidate':c} for s,c in queued], 'skippedByLimit':max(0,len(leads)-len(queued))})
        failed = [s for s in results if s.get('outcome') not in ('success','no_matches')]
        report = {'id':collected['id'], 'startedAt':collected['startedAt'], 'completedAt':stamp(), 'windowStart':str(start), 'windowEnd':str(end), 'preview':a.preview, 'outcome':'partial' if failed else 'collected', 'sources':[{'sourceId':s.get('sourceId'), 'name':s.get('name'), 'outcome':s.get('outcome'), 'candidateCount':s.get('candidateCount',0), 'httpStatus':s.get('httpStatus'), 'message':s.get('message','')} for s in results], 'candidateCount':len(leads), 'luna':{'status':'unavailable', 'limit':a.luna_limit, 'queued':len(queued), 'skippedByLimit':max(0,len(leads)-len(queued)), 'message':'No standalone Luna runner is configured; candidates remain unreviewed.'}, 'terra':{'status':'not_run', 'limit':a.terra_limit, 'used':0}, 'eventsAdded':0, 'eventsUpdated':0, 'publication':'not_attempted', 'message':'Collection only: no candidate was imported or published. Site publishing requires the Sites session workflow.'}
        reports=read(REPORTS, []); reports.append(report); write(REPORTS,reports)
        if not a.preview:
            build=subprocess.run([sys.executable,str(ROOT/'scripts/build.py')],cwd=ROOT)
            if build.returncode:
                report['outcome']='build_failed'; report['message']='Local build failed; the live site was not changed.'; reports[-1]=report; write(REPORTS,reports); return 1
        print(f"Refresh {report['id']}: {len(results)} sources, {len(failed)} deferred or failed, {len(leads)} leads; 0 events imported.")
        print(f"Local review queue: {run_dir/'model-queue.json'}")
        print('Luna/Terra and Sites publication are not available to this standalone command; see source-guides/refresh.md.')
        return 1 if failed or proc.returncode else 0
if __name__ == '__main__': raise SystemExit(main())
