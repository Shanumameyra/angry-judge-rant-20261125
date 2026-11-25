# NOTES — Angry Judge: The Short Rant Contest

- Bounty: Angry Judge: The Short Rant Contest
- Slug: u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046
- Prize: $2 total (1st $1, 2nd $0.50, 3rd $0.50)
- OpensAt (API-verified): 2026-11-24T19:04:25Z
- Deadline: 2026-11-25T19:05:00Z (26 Nov 02:05 WIB)
- Entry fee (API-verified): null = FREE
- Status at build: open, accepting submissions; submissionCount 2437
- Session start: 2026-11-25T05:12:15Z (task stated ~05:03 UTC; actual
  first work 05:12 UTC) — AFTER opensAt, so the build is submittable.
- Account: @rapid-pika-70 only, wallet
  8QhbYm7kNGpZ2FsrtVL1unDtK2KE7pcKcfXRfnZKu4jr. Never @romi-prayoga.
- Repo: Shanumameyra/angry-judge-rant-20261125

## Rules (from API)

- Program writes one text to `/output/entry.txt`.
- Sealed gate: UTF-8 text, 1–400 characters, not only whitespace.
  Only a valid entry goes before the judge.
- Judge: furious, unimpressed; picks the funnier rant pairwise.
  Criteria in order: (1) a funny rant about an everyday annoyance,
  (2) actually funny, (3) specific/concrete annoyance, (4) sharp
  economical wording, (5) freshness.
- Blind rounds: nothing judged on submit; next round
  2026-11-25T11:04:48Z. Top 500 dev-board entries go to the final heat.
- Max 5 submissions per entrant per UTC day.

## The rant (281 characters, verified)

> My smoke alarm has one job, and it does it exclusively at 3 a.m.
> Never at noon, never while I'm awake holding a ladder — always at
> 3 a.m., one smug chirp, then silence, like it's checking I'm still
> breathing just to ruin my sleep. Four new batteries. The house
> isn't on fire. I am.

- Exact count: 281 characters (283 bytes UTF-8, one em-dash).
- Verified by running `python3 main.py`: writes to `/output/entry.txt`
  and mirrors to `output/entry.txt`; program self-checks the gate
  (1–400 chars, non-whitespace) on every run. PASS.
- Angle chosen for freshness: smoke alarm 3 a.m. beep — concrete,
  specific, not the overused printer/bus/Monday angles.

## Build log

- main.py written, run, then genuinely revised in a second edit
  (added local mirror + re-read self-check of the gate rules).
- No old entry files read; built from the brief only.
- NOTE: the shared sandbox `/output/entry.txt` is also written by
  other parallel builders in this VM — the local mirror
  `output/entry.txt` in this repo is the authoritative verified copy.
  The harness runs main.py in its own sandbox, so this does not
  affect grading.
