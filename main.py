import time
import re

def load_lrc(file_path):
    """Load and parse .lrc file into a list of (timestamp, text) tuples."""
    pattern = re.compile(r"\[(\d+):(\d+\.\d+)\](.*)")
    lyrics = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = pattern.match(line.strip())
            if match:
                minutes, seconds, text = match.groups()
                # Convert timestamp to seconds
                timestamp = int(minutes) * 60 + float(seconds)
                lyrics.append((timestamp, text.strip()))
    return lyrics

def play_lyrics(lyrics):
    """Display lyrics synchronized with their timestamps in real-time."""
    start_time = time.time()
    for ts, text in lyrics:
        # Wait until the current timestamp is reached
        while time.time() - start_time < ts:
            time.sleep(0.01)
        print(text)

if __name__ == "__main__":
    lrc_file = "lyrics/diles.lrc"
    lyrics = load_lrc(lrc_file)
    play_lyrics(lyrics)