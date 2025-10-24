import time
import re
import sys

# ANSI color codes
YELLOW = '\033[93m'
RESET = '\033[0m'

def load_lrc(file_path):
    """Load and parse .lrc file into a list of (timestamp, text) tuples."""
    pattern = re.compile(r"\[(\d+):(\d+\.\d+)\](.*)")
    lyrics = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.match(line.strip())
            if match:
                minutes, seconds, text = match.groups()
                lyrics.append((int(minutes) * 60 + float(seconds), text.strip()))
    return lyrics

def play_lyrics(lyrics):
    """Display lyrics with typewriter effect synchronized with timestamps."""
    start_time = time.time()
    for ts, text in lyrics:
        while time.time() - start_time < ts:
            time.sleep(0.01)
        sys.stdout.write('\r' + ' ' * 80 + '\r')
        for char in text:
            sys.stdout.write(YELLOW + char)
            sys.stdout.flush()
            time.sleep(0.03)
        sys.stdout.write(RESET + '\n')
        sys.stdout.flush()

if __name__ == "__main__":
    lyrics = load_lrc("lyrics/diles.lrc")
    play_lyrics(lyrics)