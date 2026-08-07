# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A single-script solution to a puzzle (see `README.md`): N bulbs, all off; on press K (for K in 1..N), every bulb divisible by K is toggled. Which bulbs are lit at the end?

The whole program is `bulbs_game.py` — `simulate()` does a sieve-style pass (for each press, step through its multiples), `lit_bulbs()` filters, `format_bulbs()` renders, `main()` wires up argparse. There is no package structure, no test suite, and no build step.

## Running

```
python bulbs_game.py            # default 1000 bulbs
python bulbs_game.py -n 100 -v  # smaller board, trace every flip
```

Python 3.10+, no third-party dependencies. The system `python3` on this machine is 3.9, which the script rejects with a friendly message from its version guard; use `~/miniconda3/envs/py_313/bin/python` (or `py_310`) to actually run it.

## Conventions worth preserving

- Results go to **stdout**; the summary line and verbose trace go to **stderr**, so the bulb list stays pipeable.
- `simulate()` returns a list of length `N + 1` with index 0 as unused padding, so bulb numbers index directly.
- The math and the alternative approaches live in `README.md` — if the algorithm changes, that section is what needs to stay true.

## Checking correctness

The lit bulbs are always the perfect squares (a bulb ends on iff its divisor count is odd), and their count is `floor(sqrt(N))` — 31 for the default board, ending at 961. Any refactor can be checked against `[k*k for k in range(1, isqrt(n) + 1)]`.

## Branches

Work happens on `refactor/2026-revisit`; `master` is the default/PR target.
