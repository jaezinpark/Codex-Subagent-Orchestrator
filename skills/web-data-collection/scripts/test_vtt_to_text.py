"""Tests for vtt_to_text.py. Run: python3 -m unittest discover -s skills/web-data-collection/scripts"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from vtt_to_text import format_start, parse_cues, transcript_lines

SCRIPT = Path(__file__).resolve().parent / "vtt_to_text.py"

# Shape of a YouTube auto-caption file: word-timing tags, " " payload lines,
# 10 ms bridge cues, and each line repeated by the following cue.
# Written line by line so the single-space payload lines survive editors.
YOUTUBE_AUTO = (
    "WEBVTT\n"
    "Kind: captions\n"
    "Language: en\n"
    "\n"
    "00:00:00.000 --> 00:00:02.310 align:start position:0%\n"
    " \n"
    "hello<00:00:00.480><c> everyone</c><00:00:00.960><c> welcome</c>\n"
    "\n"
    "00:00:02.310 --> 00:00:02.320 align:start position:0%\n"
    "hello everyone welcome\n"
    " \n"
    "\n"
    "00:00:02.320 --> 00:00:05.000 align:start position:0%\n"
    "hello everyone welcome\n"
    "to<00:00:02.800><c> the</c><00:00:03.100><c> channel</c>\n"
    "\n"
    "00:00:05.000 --> 00:00:05.010 align:start position:0%\n"
    "to the channel\n"
    " \n"
    "\n"
    "00:01:05.010 --> 00:01:08.000 align:start position:0%\n"
    "to the channel\n"
    "today<00:01:05.500><c> we</c><00:01:06.000><c> build</c>\n"
)

MANUAL = """WEBVTT

NOTE written by a human
this block is not a cue

STYLE
::cue { color: white }

1
00:00:01.000 --> 00:00:03.000
<v Narrator>Tom &amp; Jerry</v>
<i>are&nbsp;back</i>

2
00:00:03.500 --> 00:00:05.000
&lt;applause&gt;
"""


def run_cli(*args, stdin=b""):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args], input=stdin, capture_output=True, check=False
    )


class TranscriptTest(unittest.TestCase):
    def test_youtube_auto_captions_are_deduplicated(self):
        lines = transcript_lines(parse_cues(YOUTUBE_AUTO))
        self.assertEqual(lines, ["hello everyone welcome", "to the channel", "today we build"])

    def test_timestamps_use_first_appearance(self):
        lines = transcript_lines(parse_cues(YOUTUBE_AUTO), timestamps=True)
        self.assertEqual(
            lines,
            [
                "[00:00:00] hello everyone welcome",
                "[00:00:02] to the channel",
                "[00:01:05] today we build",
            ],
        )

    def test_manual_captions_strip_blocks_ids_tags_and_entities(self):
        lines = transcript_lines(parse_cues(MANUAL))
        self.assertEqual(lines, ["Tom & Jerry", "are back", "<applause>"])

    def test_multi_line_rolling_window_is_deduplicated(self):
        vtt = (
            "WEBVTT\n\n00:00:00.000 --> 00:00:01.000\nA\nB\n\n"
            "00:00:01.000 --> 00:00:02.000\nA\nB\nC\n"
        )
        self.assertEqual(transcript_lines(parse_cues(vtt)), ["A", "B", "C"])

    def test_non_adjacent_repeat_is_kept(self):
        vtt = (
            "WEBVTT\n\n00:00:00.000 --> 00:00:01.000\nyes\n\n"
            "00:00:01.000 --> 00:00:02.000\nno\n\n"
            "00:00:02.000 --> 00:00:03.000\nyes\n"
        )
        self.assertEqual(transcript_lines(parse_cues(vtt)), ["yes", "no", "yes"])

    def test_crlf_and_short_timing_format(self):
        vtt = "WEBVTT\r\n\r\n01:02.500 --> 01:04.000\r\nshort form\r\n"
        self.assertEqual(
            transcript_lines(parse_cues(vtt), timestamps=True), ["[00:01:02] short form"]
        )

    def test_format_start_with_hours_and_comma(self):
        self.assertEqual(format_start("01:02:03,999"), "[01:02:03]")

    def test_no_cues_yields_nothing(self):
        self.assertEqual(transcript_lines(parse_cues("WEBVTT\n\nNOTE nothing here\n")), [])


class CliTest(unittest.TestCase):
    def test_file_with_bom(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sub.vtt"
            path.write_bytes(b"\xef\xbb\xbf" + YOUTUBE_AUTO.encode())
            result = run_cli("--timestamps", str(path))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(
            result.stdout.decode().splitlines()[0], "[00:00:00] hello everyone welcome"
        )

    def test_stdin(self):
        result = run_cli(stdin=MANUAL.encode())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.decode(), "Tom & Jerry\nare back\n<applause>\n")

    def test_missing_file_exits_2(self):
        result = run_cli("/nonexistent/sub.vtt")
        self.assertEqual(result.returncode, 2)
        self.assertIn("cannot read", result.stderr.decode())

    def test_no_text_exits_1(self):
        result = run_cli(stdin=b"WEBVTT\n\n")
        self.assertEqual(result.returncode, 1)
        self.assertIn("no subtitle text", result.stderr.decode())


if __name__ == "__main__":
    unittest.main()
