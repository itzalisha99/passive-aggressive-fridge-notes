# Notes From a Passive-Aggressive Fridge

[![make.fun](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![Rank](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/itzalisha99/passive-aggressive-fridge-notes/rank.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)
[![Reward](https://make.fun/badge/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7/itzalisha99/passive-aggressive-fridge-notes/reward.svg)](https://make.fun/bounty/u-motasimfuad-notes-from-a-passive-aggressive-fridge-83c00ad7)

A make.fun entry for **Notes From a Passive-Aggressive Fridge** — one funny
passive-aggressive note a smart fridge leaves for its owner.

## The note

> The yogurt expired on Tuesday. I kept it anyway, because unlike you, I commit to things.

The fridge tracks its inventory to the day, keeps the expired yogurt out of
sheer commitment, and turns the owner's own habit back on them in the last
five words. Dry, petty, domestic — and exactly the sort of thing a smug
appliance would keep on its door screen.

## How it works

`main.py` (Python 3, standard library only) writes the note to
`/output/entry.txt` and checks it first against the bounty gate: UTF-8 text,
1–200 characters, not only white space, a single line. It then reads the file
back and confirms it is byte-identical to the note.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
