"""
Pull YouTube transcripts for the videos tracked in research/sources.md.

Usage:
    pip install youtube-transcript-api
    python collect_youtube_transcripts.py

Writes each transcript to research/youtube-transcripts/<slug>.md, replacing
the "COLLECTED" placeholder file. Run this from a normal machine —
it needs direct internet access to youtube.com, which a locked-down sandbox
may block.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from pathlib import Path

VIDEOS = {
    "lily-ray-20for20": "gRfP9sM_ZfA",
    "nathan-gotch-7-step-checklist": "H_l6nQjrc0Y",
    "nathan-gotch-rank-everywhere": "qzMAGdzra88",
    "nathan-gotch-ai-seo-daily": "cmCafFbC1A4",
}

OUT_DIR = Path(__file__).resolve().parent.parent / "youtube-transcripts"

def main():
    api = YouTubeTranscriptApi()
    for slug, video_id in VIDEOS.items():
        out_path = OUT_DIR / f"{slug}.md"
        try:
            transcript = api.fetch(video_id)
            text = "\n".join(snippet.text for snippet in transcript.snippets)
        except Exception as e:
            print(f"[FAIL] {slug} ({video_id}): {e}")
            continue

        existing = out_path.read_text(encoding="utf-8") if out_path.exists() else ""
        header = existing.split("**Transcript status:")[0]
        out_path.write_text(
            f"{header}**Transcript status: collected.**\n\n{text}\n",
            encoding="utf-8",
        )
        print(f"[OK] {slug} -> {out_path}")

if __name__ == "__main__":
    main()
