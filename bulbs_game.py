#!/usr/bin/env python3
"""Brute-force solver for the "engineer and the bulbs" puzzle.

The puzzle
----------
There are ``N`` light bulbs (``N = 1000`` by default), numbered ``1..N``, all
of them switched off. A switch is pressed ``N`` times. On the ``K``-th press,
every bulb whose number is divisible by ``K`` flips its state: on becomes off
and off becomes on. Which bulbs are lit once the last press is done?

This module answers the question by simulation -- it literally flips every
bulb and reports what survived. See ``README.md`` for the closed-form answer
and for why the simulation is not the only way (nor the fastest one).

Usage
-----
    python bulbs_game.py             # solve for the default 1000 bulbs
    python bulbs_game.py -n 100      # solve for a smaller board
    python bulbs_game.py -v          # trace every single flip on stderr

Requires Python 3.10 or newer. It has no third-party dependencies.
"""

import sys

if sys.version_info < (3, 10):  # pragma: no cover - guard for old interpreters
    sys.exit(
        f"bulbs_game.py requires Python 3.10 or newer, "
        f"but is running on {sys.version.split()[0]}."
    )

import argparse

#: How many bulbs the original puzzle statement talks about.
DEFAULT_BULB_COUNT = 1000


def simulate(bulb_count: int = DEFAULT_BULB_COUNT, *, verbose: bool = False) -> list[bool]:
    """Press the switch ``bulb_count`` times and return the resulting states.

    Args:
        bulb_count: How many bulbs are on the board. Bulbs are numbered
            ``1..bulb_count`` and every one of them starts switched off.
        verbose: When true, report each individual flip on stderr. Handy for
            following the puzzle by hand on a small board, unbearably chatty
            on the full one (the default board performs ~7500 flips).

    Returns:
        A list of length ``bulb_count + 1`` where ``states[i]`` tells whether
        bulb ``i`` is lit. Index ``0`` is unused padding so that a bulb's
        number can be used as its index directly.
    """
    if bulb_count < 0:
        raise ValueError(f"bulb_count must not be negative, got {bulb_count}")

    # Index 0 is a placeholder for the non-existent "bulb zero"; it keeps the
    # bulb numbers and the list indices aligned, which is worth one wasted
    # boolean.
    states = [False] * (bulb_count + 1)

    for press in range(1, bulb_count + 1):
        # Only the multiples of `press` are affected, so jump straight to them
        # instead of asking every bulb whether it is divisible. This is what
        # turns the naive O(N^2) scan into an O(N log N) walk.
        for bulb in range(press, bulb_count + 1, press):
            states[bulb] = not states[bulb]
            if verbose:
                new_state = "on" if states[bulb] else "off"
                print(
                    f"press {press:>4}: bulb {bulb:>4} divisible by {press:>4}"
                    f" -> switched {new_state}",
                    file=sys.stderr,
                )

    return states


def lit_bulbs(states: list[bool]) -> list[int]:
    """Return the numbers of the bulbs that are lit, in ascending order.

    Args:
        states: The board as returned by :func:`simulate`, i.e. with the
            unused padding entry at index ``0``.
    """
    return [bulb for bulb, is_lit in enumerate(states) if is_lit and bulb > 0]


def format_bulbs(bulbs: list[int]) -> str:
    """Render bulb numbers in set notation, e.g. ``{1, 4, 9, 16}``."""
    return "{" + ", ".join(str(bulb) for bulb in bulbs) + "}"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse the command line. ``argv`` defaults to :data:`sys.argv`."""
    parser = argparse.ArgumentParser(
        description=__doc__.split("\n\n", maxsplit=1)[0],
        epilog="The lit bulbs always turn out to be the perfect squares -- "
        "see README.md for the reason why.",
    )
    parser.add_argument(
        "-n",
        "--count",
        type=int,
        default=DEFAULT_BULB_COUNT,
        metavar="N",
        help=f"number of bulbs on the board (default: {DEFAULT_BULB_COUNT})",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="print every flip on stderr while simulating",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Run the solver as a command line program and return its exit code."""
    args = parse_args(argv)

    if args.count < 0:
        print("error: --count must not be negative", file=sys.stderr)
        return 2

    states = simulate(args.count, verbose=args.verbose)
    bulbs = lit_bulbs(states)

    print(format_bulbs(bulbs))
    print(
        f"{len(bulbs)} of {args.count} bulbs are lit at the end.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
