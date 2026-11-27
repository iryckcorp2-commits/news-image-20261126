#!/usr/bin/env python3
"""Copy entry.png to the make.fun output directory."""

import os
import shutil
import sys


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, "entry.png")
    if not os.path.isfile(source):
        print("entry.png not found next to main.py", file=sys.stderr)
        return 1
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")
    shutil.copyfile(source, destination)
    print("Copied entry.png to " + destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
