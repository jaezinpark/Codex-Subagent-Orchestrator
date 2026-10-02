#!/usr/bin/env python3
"""Convert a WebVTT subtitle file into plain transcript text.

Strips the header, NOTE/STYLE/REGION blocks, cue identifiers, timing lines,
inline timestamp and styling tags, and decodes HTML entities. YouTube
auto-generated captions repeat each line across rolling cues; lines a cue
repeats from the end of the transcript so far are dropped, so each spoken
line appears once.

Usage:
    vtt_to_text.py [--timestamps] [FILE]    # FILE defaults to stdin ("-")

Exit status: 0 on success, 1 when the input has no subtitle text,
2 when the input cannot be read.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass, field

_TIMING = re.compile(r"^\s*((?:\d+:)?\d{1,2}:\d{2}[.,]\d{3})\s+-->\s+")
_TAG = re.compile(r"<[^>]*>")
_SPACE = re.compile(r"\s+")


@dataclass
class Cue:
    start: str
    lines: list[str] = field(default_factory=list)


def parse_cues(text: str) -> list[Cue]:
    """Return cues with their raw payload lines; non-cue blocks are skipped."""
    cues: list[Cue] = []
    in_cue = False
    for line in text.splitlines():
        match = _TIMING.match(line)
        if match:
            cues.append(Cue(start=match.group(1)))
            in_cue = True
        elif line == "":
            # Only a truly empty line ends a cue; YouTube payloads contain " " lines.
            in_cue = False
        elif in_cue:
            cues[-1].lines.append(line)
    return cues


def clean_line(raw: str) -> str:
    text = html.unescape(_TAG.sub("", raw))
    return _SPACE.sub(" ", text).strip()


def format_start(start: str) -> str:
    parts = start.replace(",", ".").split(":")
    seconds = float(parts[-1]) + 60 * int(parts[-2])
    if len(parts) == 3:
        seconds += 3600 * int(parts[0])
    whole = int(seconds)
    return f"[{whole // 3600:02d}:{whole % 3600 // 60:02d}:{whole % 60:02d}]"


def _overlap(emitted: list[str], current: list[str]) -> int:
    """Length of the longest prefix of `current` that repeats the tail of `emitted`."""
    for size in range(min(len(emitted), len(current)), 0, -1):
        if emitted[-size:] == current[:size]:
            return size
    return 0


def transcript_lines(cues: list[Cue], timestamps: bool = False) -> list[str]:
    emitted: list[str] = []
    output: list[str] = []
    for cue in cues:
        current = [line for line in map(clean_line, cue.lines) if line]
        for line in current[_overlap(emitted, current) :]:
            emitted.append(line)
            output.append(f"{format_start(cue.start)} {line}" if timestamps else line)
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Convert WebVTT subtitles to plain text.")
    parser.add_argument("file", nargs="?", default="-", help="WebVTT file, or - for stdin")
    parser.add_argument(
        "--timestamps",
        action="store_true",
        help="prefix each line with [HH:MM:SS] of the cue where it first appears",
    )
    args = parser.parse_args(argv)

    try:
        if args.file == "-":
            text = sys.stdin.buffer.read().decode("utf-8-sig")
        else:
            with open(args.file, encoding="utf-8-sig") as handle:
                text = handle.read()
    except (OSError, UnicodeDecodeError) as error:
        print(f"vtt_to_text: cannot read {args.file}: {error}", file=sys.stderr)
        return 2

    lines = transcript_lines(parse_cues(text), timestamps=args.timestamps)
    if not lines:
        print(f"vtt_to_text: no subtitle text found in {args.file}", file=sys.stderr)
        return 1
    sys.stdout.write("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
