#!/usr/bin/env python3
"""Print a compact source-specific brief for a cheap extraction run; no network or writes."""
import argparse
import datetime
import json
import pathlib
import re
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parents[1]


def make_prompt(audit, profile, domain, start, end):
    row = next((r for r in audit['sources'] if r['domain'] == domain), None)
    if not row:
        raise ValueError('Source is not in the audited inventory: ' + domain)
    if row['outcome'] == 'excluded':
        return f"Skip {domain}: excluded by the saved activity blacklist. Recheck the profile before any research.\n"
    # A source can be a broad directory with an archived excluded listing.
    # Never select that listing as the next run's entry just because it has
    # an access observation. Prefer an explicit reviewed entry when supplied.
    candidates = [a for a in row['attempts'] if not re.search(
        r'\b(?:excluded|blacklist(?:ed)?)\b', str(a['observedFields'].get('access', '')), re.I)]
    good = [a for a in candidates if not a.get('error') and any(k != 'title' and v for k, v in a['observedFields'].items())]
    readable = [a for a in candidates if not a.get('error')]
    urls = ([row['entryUrl']] if row.get('entryUrl') else
            list(dict.fromkeys(a['url'] for a in (good or readable or candidates)))[:2])
    if not urls:
        raise ValueError('No allowed public entry is recorded; review the source guide before generating a brief')
    lines = [f'Check {domain} for Amsterdam activities from {start} through {end}.',
             f"Use {profile['timezone']}. This guide was spot-checked {audit['checkedAt']}; verify freshness and the displayed year.",
             '', 'Public entry: ' + ' ; '.join(urls), '']
    if row['quickStart']:
        lines += ['Source steps:'] + [f'{i}. {step}' for i, step in enumerate(row['quickStart'], 1)] + ['']
    lines += ['Last route finding: ' + row['issue'], 'Next check: ' + row['recommendedNextStep'], '',
              'Return a small evidence packet: title, exact date/year, start/end, venue/address, regular single-person price '
              'and extras, joining rules, spoken language, source URL, and unknowns. No recurrence expansion; no language '
              'inferred from webpage language. Keep free, paid, tips, and donation separate; ClassPass credits are not EUR.',
              f"Preferred hours: weekends any time; weekdays start >= {profile['weekdayEveningStart']}, or explicit same-day end <= {profile['weekdayMorningEnd']}.",
              'Skip saved blacklist groups: ' + ', '.join(profile.get('blacklist', [])) +
              ('; custom keywords: ' + ', '.join(profile['customKeywords']) if profile.get('customKeywords') else '') + '.',
              'Try public text extraction first, then the normal browser if needed. Stop at login/security/checkout gates; '
              'do not book, pay, create accounts, contact anyone or repeatedly retry the same failure. Missing prices stay unknown. '
              'Log exact failures and untested steps. Android requires the separate approved bounded workflow. '
              'Do not change canonical data; prepare a reviewed batch. Read the full source guide only for a specific unresolved question.', '']
    return '\n'.join(lines).replace('{start_date}', str(start)).replace('{end_date}', str(end))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('domain')
    p.add_argument('--start-date', required=True, type=datetime.date.fromisoformat)
    p.add_argument('--end-date', required=True, type=datetime.date.fromisoformat)
    args = p.parse_args()
    if args.end_date < args.start_date:
        p.error('End date precedes start date')
    domain = (urlparse(args.domain if '://' in args.domain else 'https://' + args.domain).hostname or '').lower().removeprefix('www.')
    audit = json.loads((ROOT / 'data/source-audit.json').read_text())
    profile = json.loads((ROOT / 'data/preferences.json').read_text())
    try:
        print(make_prompt(audit, profile, domain, args.start_date, args.end_date), end='')
    except ValueError as e:
        p.error(str(e))


if __name__ == '__main__':
    main()
