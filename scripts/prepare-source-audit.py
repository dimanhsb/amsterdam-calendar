#!/usr/bin/env python3
"""Prepare a fresh Luna audit without overwriting a previous run's evidence."""
import argparse
import datetime
import hashlib
import importlib.util
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('guides', ROOT / 'scripts/source-guides.py')
guides = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guides)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output', required=True, type=pathlib.Path)
    p.add_argument('--checked-date', required=True, type=datetime.date.fromisoformat)
    p.add_argument('--start-date', required=True, type=datetime.date.fromisoformat)
    p.add_argument('--end-date', required=True, type=datetime.date.fromisoformat)
    p.add_argument('--shards', type=int, default=3)
    args = p.parse_args()
    if args.shards < 1 or args.end_date < args.start_date:
        p.error('Use a positive shard count and an ordered date window')
    out = args.output.resolve()
    if out.exists() and any(out.iterdir()):
        p.error('Output directory must be empty; audit baselines must not be overwritten')
    sources = guides.load_sources()
    profile = json.loads((ROOT / 'data/preferences.json').read_text())
    excluded = set().union(*(guides.BLACKLIST_DOMAIN_RULES.get(rule, set()) for rule in profile.get('blacklist', [])))
    rows = []
    for n, (domain, observations) in enumerate(sorted(sources.items())):
        name = guides.filename(domain)
        path = ROOT / 'source-guides' / name
        if not path.is_file():
            p.error(f'Missing {name}; generate/review source guides first')
        rows.append(dict(domain=domain, guide=name, guideSha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                         urls=[s['url'] for s in observations], sources=observations,
                         # An aggregator can have only blacklisted saved links
                         # and still publish many allowed activities.
                         excluded=domain in excluded, shard=n % args.shards + 1))
    out.mkdir(parents=True, exist_ok=True)
    def write(name, data):
        (out / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    write('manifest.json', dict(createdAt=str(args.checked_date), startDate=str(args.start_date), endDate=str(args.end_date),
                               profile=profile, scope='All saved source, idea, provider and existing per-website guide domains; excluded activities receive a guide-only review.', sources=rows))
    for shard in range(1, args.shards + 1):
        write(f'shard-{shard}.json', [r for r in rows if r['shard'] == shard])
    brief = (ROOT / 'research/source-audit/BRIEF.md').read_text()
    brief = brief.replace('18 October 2026', args.checked_date.strftime('%d %B %Y').lstrip('0'))
    brief = brief.replace('2026-10-18', str(args.checked_date))
    brief = brief.replace('19 Oct–30 Nov 2026', f'{args.start_date}–{args.end_date}')
    (out / 'BRIEF.md').write_text(brief)
    print(f'Prepared {len(rows)} websites in {args.shards} shards at {out}; prior results unchanged.')


if __name__ == '__main__':
    main()
