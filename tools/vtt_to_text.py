"""Convert a .vtt caption file to clean plain text (dedup rolling auto-caption lines).

Usage: python tools/vtt_to_text.py raw/youtube/chan/2023-01-01-abc.en.vtt
Writes the .txt next to the input file.
"""
import re
import sys
from pathlib import Path


def vtt_to_text(path: Path) -> Path:
    lines_out: list[str] = []
    prev = ""
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if (not line or line == "WEBVTT" or "-->" in line
                or line.startswith(("Kind:", "Language:", "NOTE"))
                or re.fullmatch(r"\d+", line)):
            continue
        line = re.sub(r"<[^>]+>", "", line)  # strip inline timing/karaoke tags
        if line and line != prev:
            lines_out.append(line)
            prev = line
    out = path.with_suffix(".txt")
    out.write_text("\n".join(lines_out) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(vtt_to_text(Path(arg)))
