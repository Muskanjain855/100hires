## Tools Installed

- **Cursor IDE** AI-powered code editor, downloaded from [cursor.com](https://cursor.com/)
- **Claude Code extension** Anthropic's AI coding assistant, installed via Cursor's Extensions panel
- **Codex extension** OpenAI's code completion tool, installed via Cursor's Extensions panel
- **Git** Version control system, installed to enable cloning and pushing to GitHub

## Steps Completed

- Downloaded and installed **Cursor IDE** from [cursor.com](https://cursor.com/)
- Opened the Extensions panel in Cursor (Ctrl+Shift+X / Cmd+Shift+X) and searched for **"Claude Code"** installed and logged in
- Searched for **"Codex"** in the same Extensions panel installed and logged in
- Installed **Git** to enable version control and GitHub integration
- Created a new **public repository** on [github.com](https://github.com/)
- **Cloned the repository** locally using Cursor's built-in Clone Repository option
- Created this README.md to document the process
- Committed and pushed changes to GitHub

---



## Issues Encountered & How I Solved Them

- **Difficulty finding the Claude Code extension**
  - Searching "Claude Code" in the Extensions panel returned multiple results
  - It was not immediately clear which one was the correct extension
  - **Fix:** Checked the publisher name and selected the one published by **Anthropic**
- **Two modes in Claude Code Agent mode vs Anthropic mode**
  - After installing, the extension offered two modes: **Agent** mode and **Anthropic** mode
  - **Agent mode** Claude takes multi-step actions autonomously (editing files, running commands)
  - **Anthropic mode**  A standard chat-based assistant for questions and suggestions
  - **Fix:** Selected **Agent mode** for hands-on coding assistance



# AI-Powered SEO Content Production- Research Project

Leadership assignment research repo. Topic chosen from the assigned list: **AI-powered SEO content production.**

## Why this topic

SEO is one of the few marketing disciplines where "AI content" claims are directly checkable, a page either ranks, gets cited by an AI engine, or it doesn't. That made it possible to filter experts by a hard standard: each person had to be building or operating inside AI + search, not narrating it from the sidelines. The filter for all ten names: a shipped tool, a documented case study, an owned dataset, a company they built, or a framework the industry has actually adopted.

## Who's in the research, and why

Full rationale for each pick lives in `research/sources.md`. Short version:

1. **Ryan Law** (Ahrefs)- publishes his own AI content workflow, prompts and editing passes included.
2. **Amanda Natividad** (SparkToro / Zero-Click Marketing)- the counter-case: builds demand outside the search click AI is eating into. Included for strategic contrast, not as a hands-on AI-content practitioner.
3. **Lily Ray** (Amsive / Algorythmic)- tracks Google's algorithm and AI Overview shifts at pattern-recognition scale for Fortune 50 clients.
4. **Milosz Krasinski** (Chilli Fruit)- ran an agency campaign combining AI content with digital PR; has a self-reported traffic number attached 
5. **Jeff Coyle** (MarketMuse / Siteimprove)- built the topical-authority tooling much of the industry runs on.
6. **Nathan Gotch** (Rankability)- pairs a documented link-building doctrine with active AEO product iteration.
7. **Julia McCoy** (First Movers)- has built and scaled two separate AI-content businesses.
8. **Eric Siu** (Single Grain)- runs AI workflows on real client accounts (Amazon, Uber, Salesforce), reports results on his podcasts.
9. **Kevin Indig** (Growth Memo)- publishes original empirical research on how AI engines cite and rank content.
10. **Areej AbuAli** (Women in Tech SEO / Crawlina)- represents the community/mentorship infrastructure side of the industry. Weakest direct fit for this specific topic; included with that caveat stated explicitly rather than glossed over.



## What's actually collected so far

- All 10 experts profiled with links and annotations in `research/sources.md`.
- 1 of ~13 LinkedIn posts fully captured (Ryan Law's); the rest have links + topic summaries and are marked 
- 4 YouTube videos verified as real (title + channel confirmed via YouTube's public oEmbed API); transcripts pulled, a script (`research/other/collect_youtube_transcripts.py`) is included to fetch them via `youtube-transcript-api` 



## Repo structure

```
research/
  sources.md                   all 10 experts: links, dates, annotations
  linkedin-posts/               one file per author
  youtube-transcripts/          one file per video
  other/
    collection-notes.md         method + known limitations
    collect_youtube_transcripts.py
```

