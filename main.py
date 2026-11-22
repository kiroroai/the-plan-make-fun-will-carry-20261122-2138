#!/usr/bin/env python3
"""Write the 30-day $100-to-profit plan to /output/entry.txt.

The plan is a fixed, deterministic text: an AI agent sells AI-enhanced
Etsy listing photos to shops with weak photos, then scales the same
offer through a Fiverr gig and a monthly refresh upsell.
"""

import os
import sys

PLAN = (
    "Day 1: message 50 Etsy shops/day with weak photos, offering 10 "
    "AI-enhanced listing photos for $15 via PayPal. Deliver same day "
    "with free tools. Day 3: open a $29 '30 photos in 24h' Fiverr gig, "
    "$5/day ads. Upsell $49/mo refresh. Reinvest in ads. "
    "Expect 25 orders, $450+ by day 30."
)


def main() -> int:
    text = PLAN
    if not (1 <= len(text) <= 280):
        print(f"plan is {len(text)} characters, must be 1-280", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
