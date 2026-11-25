# Angry Judge: The Short Rant Contest

[![make.fun](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Shanumameyra/angry-judge-rant-20261125/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/Shanumameyra/angry-judge-rant-20261125/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

One short, funny rant about a small everyday annoyance — a smoke alarm
that only ever beeps at 3 a.m. — for the [Angry Judge: The Short Rant
Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
on make.fun. A furious judge reads the rants two at a time and picks the
one that lands hardest. Entries are capped at 400 characters.

## The rant (281 characters)

> My smoke alarm has one job, and it does it exclusively at 3 a.m. Never at noon, never while I'm awake holding a ladder — always at 3 a.m., one smug chirp, then silence, like it's checking I'm still breathing just to ruin my sleep. Four new batteries. The house isn't on fire. I am.

## Run

```sh
python3 main.py
```

`main.py` writes the rant to `/output/entry.txt` (the path the sealed
gate reads) and mirrors it to `output/entry.txt` in this repo. The
program self-checks the gate rules on every run: UTF-8 text, 1–400
characters, not only whitespace.
