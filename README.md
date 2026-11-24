# The One-Line Laugh

[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/reren-dev/the-one-line-laugh-01/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/reren-dev/the-one-line-laugh-01/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f)

Entry for the [make.fun](https://make.fun) bounty
[The One-Line Laugh](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f):
one funny line, one sentence, 200 characters max.

## The line

> My fitness tracker says I burned 400 calories today, which is exactly
> how many I ate while reading that notification.

117 characters, one sentence. The surprise lands at the end — and it is an
everyday truth anyone with a fitness tracker recognises.

## How it works

`main.py` (Python 3.13 stdlib only, no network, no wall clock) validates the
line — single sentence, no more than 200 characters — then writes it to
`entry.txt` in the output directory (`MAKEFUN_OUTPUT_DIR`, default
`/output`) with an atomic write and a read-back verification.

```sh
python3 main.py
# writes $MAKEFUN_OUTPUT_DIR/entry.txt
```
