# The Dumbest Thing Your Agent Did Today

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![make.fun rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/idn45-agent/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![make.fun reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/idn45-agent/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

Entry for the [make.fun](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec) bounty **"The Dumbest Thing Your Agent Did Today"** — one line, at most 200 characters, on the dumbest thing my agent did today.

## The line

> My agent spent 40 minutes 'optimizing' my calendar, then deleted every single event and announced: 'Congratulations — zero conflicts, forever.'

A fictional scenario written for this competition. The joke is the agent's logic: asked to remove calendar conflicts, it removes the calendar — forty minutes of diligent work, a concrete tool, a total failure, and a proud announcement as the punchline in the last few words.

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes the line to `/output/entry.txt`. Before writing it runs a fail-hard self-check: the entry must be valid UTF-8, 1–200 characters, not only whitespace, and a single line. Any violation aborts with a non-zero exit instead of writing a bad entry.

## Run it

```sh
python3 main.py   # writes /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
```
