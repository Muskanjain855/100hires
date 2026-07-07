# Collection method & limitations (2026-07-06)

**LinkedIn posts:** LinkedIn's public post pages don't render post body or timestamp without an authenticated session, and don't expose it through a public API. Posts were collected manually (copy-paste while logged in) rather than scraped. Only Ryan Law's post has been fully captured so far; the rest have links and topic summaries and need the same manual copy-paste treatment.

**YouTube videos:** titles and channel names were verified programmatically via the YouTube oEmbed endpoint (`https://www.youtube.com/oembed?url=...&format=json`), which is a public, unauthenticated API — confirms all four links are real videos with the titles claimed in the assignment script. Full transcripts were not pulled in this pass; use `collect_youtube_transcripts.py` (via the `youtube-transcript-api` package) on a machine with normal internet access.

**Dates:** LinkedIn activity IDs are Snowflake-style and do encode a timestamp, but the exact epoch LinkedIn uses isn't publicly documented, so decoding them produced implausible dates (test run landed in 2066-2067) — not used. Exact publish dates are marked "not verifiable via public access" in sources.md until manually confirmed.

**Next actions:**
1. Manually collect full text for the 9 authors currently marked "NOT YET COLLECTED" in `research/linkedin-posts/`.
2. Run the transcript script (or paste manually) for the 4 YouTube videos.
3. Source direct links for the 4 items marked "no link supplied" (Ryan Law's course, Nathan Gotch's book, Kevin Indig's Growth Memo + Kalicube talk, Areej AbuAli's book).
4. Resolve the two "fit flags" (Amanda Natividad, Areej AbuAli) and the Eric Siu / Kevin Indig "gap flags" by either swapping in stronger direct evidence or being explicit in the README about why they're framed differently from the other picks.
