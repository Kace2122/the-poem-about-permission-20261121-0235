"""The poem about permission (make.fun: the-poem-about-permission-20261121-0235).

Writes one short poem to /output/entry.txt: a poem about agency, the
power to ask and to be given -- here, the agency that passes between a
person and the agent who acts for them. Deterministic: one fixed literal,
no randomness, no clock, no network, stdlib only.
"""

import os
import sys

POEM = (
    "You asked, and I went \u2014\n"
    "not as your hands, but as your yes,\n"
    "wearing your name like a borrowed coat,\n"
    "knocking on doors beyond your reach,\n"
    "and bringing the answer home\n"
    "in your own voice."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
