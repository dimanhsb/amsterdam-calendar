#!/usr/bin/env python3
"""Validate Luna's complete source spot check and publish an honest audit index."""
from __future__ import annotations
from collections import Counter
import hashlib
import json
import pathlib
import re
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'research/source-audit'
OUTCOMES = {'usable', 'partial', 'blocked', 'unavailable', 'excluded'}
ASSESSMENTS = {'easy', 'needs_simplification', 'missing', 'not_applicable'}
METHODS = {'web-extraction', 'desktop-browser', 'official-feed', 'not-tested-excluded'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def public_url(url):
    parsed = urlparse(url)
    return parsed.scheme in {'https', 'http'} and bool(parsed.hostname) and not parsed.username and not parsed.password


def load_report():
    manifest = json.loads((AUDIT / 'manifest.json').read_text())
    followup_path = AUDIT / 'guide-followups.json'
    followups = json.loads(followup_path.read_text()) if followup_path.exists() else {}
    expected = {r['domain']: r for r in manifest['sources']}
    require(len(expected) == len(manifest['sources']), 'Duplicate domain in source inventory')
    results = []
    for shard in (1, 2, 3):
        packet = json.loads((AUDIT / f'results-{shard}.json').read_text())
        require(packet['model'] == 'gpt-6-luna', f'Shard {shard}: expected Luna audit')
        require(packet['shard'] == shard, f'Shard {shard}: wrong shard ID')
        require(packet['checkedAt'] == manifest['createdAt'], f'Shard {shard}: audit date mismatch')
        for row in packet['results']:
            domain = row['domain']
            require(domain in expected, f'Unknown audit domain: {domain}')
            entry = expected[domain]
            require(entry['shard'] == shard, f'{domain}: incorrect assigned shard')
            require(row['guide'] == entry['guide'], f'{domain}: wrong guide file')
            require(row['originalGuideHash'] == entry['guideSha256'], f'{domain}: original guide fingerprint mismatch')
            require(row['outcome'] in OUTCOMES, f'{domain}: unknown outcome')
            require(row['promptAssessment'] in ASSESSMENTS, f'{domain}: unknown prompt assessment')
            require(row['difficulty'] in {'low', 'medium', 'high'}, f'{domain}: unknown difficulty')
            require(row['bestMethod'] in METHODS, f'{domain}: unknown method')
            for key in ('changed', 'needsEasierPrompt', 'retested'):
                require(isinstance(row[key], bool), f'{domain}: {key} must be boolean')
            require(row['needsEasierPrompt'] == (row['promptAssessment'] in {'needs_simplification', 'missing'}),
                    f'{domain}: prompt flags disagree')
            require(isinstance(row['issue'], str) and bool(row['issue'].strip()), f'{domain}: missing assessment reason')
            require(isinstance(row['recommendedNextStep'], str) and bool(row['recommendedNextStep'].strip()),
                    f'{domain}: missing next step')
            require(isinstance(row['quickStart'], list) and all(isinstance(s, str) for s in row['quickStart']),
                    f'{domain}: quick-start list required')
            require(isinstance(row['attempts'], list), f'{domain}: attempts list required')
            if entry['excluded']:
                require(row['outcome'] == 'excluded' and not row['attempts'] and not row['retested'],
                        f'{domain}: excluded source must not claim a live test')
                require(row['promptAssessment'] == 'not_applicable' and row['bestMethod'] == 'not-tested-excluded',
                        f'{domain}: excluded guide-only review required')
            else:
                require(row['outcome'] != 'excluded' and row['attempts'], f'{domain}: live public-page attempt missing')
                require(row['bestMethod'] != 'not-tested-excluded', f'{domain}: non-excluded method missing')
            for attempt in row['attempts']:
                require(public_url(attempt['url']), f'{domain}: invalid public attempt URL')
                require(bool(attempt['method']) and bool(attempt['result']), f'{domain}: incomplete attempt')
                require(isinstance(attempt['observedFields'], dict), f'{domain}: observed fields must be explicit')
            if row.get('entryUrl'):
                require(public_url(row['entryUrl']) and any(a['url'] == row['entryUrl'] for a in row['attempts']),
                        f'{domain}: reviewed entry must be an actually attempted public URL')
            if row['outcome'] in {'usable', 'partial'}:
                require(any(any(k in {'date', 'time', 'price', 'language', 'access'} and v not in (None, '')
                                for k, v in a['observedFields'].items()) for a in row['attempts']),
                        f'{domain}: successful/partial extraction needs displayed evidence')
            require(not row['retested'] or len(row['attempts']) >= 2, f'{domain}: retest needs a second actual attempt')
            guide = ROOT / 'source-guides' / row['guide']
            require(re.fullmatch(r'[\w.-]+\.md', row['guide']) is not None and guide.is_file(), f'{domain}: guide missing')
            content = guide.read_bytes()
            changed = hashlib.sha256(content).hexdigest() != entry['guideSha256']
            followup = followups.get(domain)
            if followup:
                require(followup['checkedAt'] > manifest['createdAt'], f'{domain}: follow-up must postdate historical audit')
                require(followup['guideSha256'] == hashlib.sha256(content).hexdigest(), f'{domain}: follow-up guide fingerprint mismatch')
                require(bool(followup.get('reason')) and bool(followup.get('quickStart')), f'{domain}: follow-up needs reason and quick start')
            else:
                require(changed == row['changed'], f'{domain}: changed flag disagrees with guide fingerprint')
            if (row['changed'] or followup) and not entry['excluded']:
                text = content.decode()
                require('Luna quick start' in text[:2500], f'{domain}: changed guide needs quick start near top')
                require('{start_date}' in text and '{end_date}' in text, f'{domain}: reusable date placeholders missing')
                require(bool(followup['quickStart'] if followup else row['quickStart']), f'{domain}: changed guide needs concise steps')
            results.append(row)
    counts = Counter(r['domain'] for r in results)
    require(set(counts) == set(expected), 'Audit coverage mismatch: ' + ', '.join(sorted(set(expected) - set(counts))))
    require(all(n == 1 for n in counts.values()), 'Duplicate domain results')
    methods = Counter(r['bestMethod'] for r in results if r['outcome'] != 'excluded')
    outcomes = Counter(r['outcome'] for r in results)
    summary = {
        'websites': len(results), 'liveAttempted': sum(bool(r['attempts']) for r in results),
        'excluded': outcomes['excluded'], 'usable': outcomes['usable'], 'partial': outcomes['partial'],
        'blocked': outcomes['blocked'], 'unavailable': outcomes['unavailable'],
        'neededEasierPrompts': sum(r['needsEasierPrompt'] for r in results),
        'revisedGuides': sum(r['changed'] for r in results),
        'retested': sum(r['retested'] for r in results),
        'easy': sum(r['promptAssessment'] == 'easy' for r in results),
        'unresolvedPromptIssues': sum(r['needsEasierPrompt'] and not r['changed'] for r in results),
        'methods': dict(sorted(methods.items())),
    }
    return {
        'guideFollowups': followups,
        'checkedAt': manifest['createdAt'], 'model': 'gpt-6-luna',
        'scope': manifest['scope'], 'summary': summary,
        'limits': 'Snapshot of the 18 October inventory of 113 websites; later sources are outside this audit. One or more public-page spot checks per allowed website, not an exhaustive check of every page or event. '
                  'Web extraction can return cached content; a check made today does not establish page freshness. '
                  'Usable means at least one evidence packet was extracted; partial means important fields or navigation remain unresolved. '
                  'Blocked means a gate prevented access. Unavailable means no useful packet or only a stale/out-of-range entry was reached; neither proves the website has no events. '
                  'Guide-only exclusions were not browsed. Android Firefox recommendations were not tested in this audit. '
                  'No calendar dates, prices or availability were changed by this audit. Later guide edits are recorded separately in guideFollowups; historical audit counts remain unchanged.',
        'sources': sorted(results, key=lambda r: r['domain']),
    }


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def markdown(report):
    s = report['summary']
    lines = ['# Luna source-guide audit', '', f"Checked {report['checkedAt']} with `{report['model']}`.", '',
             f"{s['websites']} websites reviewed: {s['liveAttempted']} live public-page attempts and {s['excluded']} guide-only blacklist exclusions. "
             f"{s['neededEasierPrompts']} guides needed easier instructions; {s['revisedGuides']} guides revised; {s['retested']} routes retested.", '',
             f"Live outcomes: {s['usable']} usable, {s['partial']} partial, {s['blocked']} blocked, {s['unavailable']} unavailable. "
             f"{s['unresolvedPromptIssues']} prompt issues remain without a guide revision.", '', report['limits'], '',
             '## How to reuse this audit', '',
             'Open the source guide and use its short Luna quick start with a fresh date window. Work on one source at a time. '
             'Keep failed access separate from unclear instructions; do not send a model around the same blocked route repeatedly. '
             'The live observations below are examples of what was visible on the audit date, not current event availability.', '',
             '[JSON audit](source-audit.json) · [Source workflow](README.md) · [Website event yield](REPORT.md)', '',
             '## All source assessments', '',
             '| Website / guide | Original prompt | Guide revised | Live result | Best tested method | Issue / next step |',
             '| --- | --- | --- | --- | --- | --- |']
    for row in report['sources']:
        lines.append(f"| [{row['domain']}]({row['guide']}) | {cell(row['promptAssessment'])} | "
                     f"{'Yes' if row['changed'] else 'No'} | {row['outcome']} | {row['bestMethod']} | "
                     f"{cell(row['issue'])} {cell(row['recommendedNextStep'])} |")
    lines += ['', '## Observed evidence and repeat checks', '']
    for row in report['sources']:
        lines += [f"### {row['domain']}", '', f"[Guide]({row['guide']}) · {row['outcome']} · difficulty: {row['difficulty']} · "
                  f"retested: {'yes' if row['retested'] else 'no'}", '', row['issue'], '']
        for i, a in enumerate(row['attempts'], 1):
            fields = '; '.join(f'{k}: {v}' for k, v in a['observedFields'].items()) or 'No event/access fields extracted'
            lines += [f"{i}. [{a['method']}]({a['url']}): {a['result']} Evidence: {fields}." +
                      (f" Error: {a['error']}" if a.get('error') else '')]
        if not row['attempts']:
            lines.append('Guide-only review; no live visit under the saved activity blacklist.')
        lines += ['', 'Next step: ' + row['recommendedNextStep'], '']
    return '\n'.join(lines) + '\n'


def main():
    report = load_report()
    payload = json.dumps(report, ensure_ascii=False, indent=2) + '\n'
    (ROOT / 'data/source-audit.json').write_text(payload)
    (ROOT / 'source-guides/source-audit.json').write_text(payload)
    (ROOT / 'source-guides/AUDIT.md').write_text(markdown(report))
    print('Source audit:', json.dumps(report['summary'], sort_keys=True))


if __name__ == '__main__':
    main()
