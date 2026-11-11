<p align="center"><img src="site/assets/banner.svg" width="1200" alt="/brag — You built it. Now brag."></p>

# /brag Guide — You built it. Now brag.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Upstream](https://img.shields.io/badge/upstream-latent--spaces%2Fbrag-blue)](https://github.com/latent-spaces/brag)
[![Status](https://img.shields.io/badge/status-live-brightgreen)]()
![Language](https://img.shields.io/badge/lang-EN%20%2B%20%E1%80%99%E1%80%BC%E1%80%94%E1%80%BA%E1%80%99%E1%80%AC-green)

> **Live.** https://brag-guide.funapp.live — verified steps only.

Use [**/brag**](https://github.com/latent-spaces/brag) with Muse: your Muse
turns the project you just built into a short launch video — the open-source
agent skill by [latent-spaces](https://github.com/latent-spaces) (Shunit Haviv
Hakimi), MIT. One command. No video editor. Your Muse does the work.

## Quick start

```bash
# Codex
codex plugin marketplace add latent-spaces/brag
codex plugin add brag@brag

# Claude Code
/plugin marketplace add latent-spaces/brag
/plugin install brag@brag

# Any other agent
npx skills add https://github.com/latent-spaces/brag --skill brag
```

Then, inside any project:

```bash
/brag
```

Your video appears in `brag-output/brag.mp4`.

## What's inside

| Path | What it is |
|---|---|
| `site/index.html` | The guide website — 8 tabbed sections, English + Burmese toggle |
| `site/assets/brag.mp4` | The verified PocketLab demo video (21s, 1920×1080, 30fps) |
| `site/assets/brag.jpg` | The demo poster frame |
| `docs/` | The same content as short Markdown chapters, one file per section |
| `scripts/` | Builders for the site and the Burmese strings |
| `assets/banner.svg` | Animated banner art |

## The method — two phases

1. **Get your Muse ready.** Install /brag + Hyperframes on the Muse's own
   machine, prove it with a test render on a bundled example, show the test
   video and the check result. Make nothing real yet.
2. **Give it your project.** App name + repo link. The Muse makes the video,
   shows video + frames first, you review, then you download and post it
   yourself. One video, one Muse at a time.

## Verified, not promised

Every step in this guide was run end-to-end on a test machine on 2026-11-10:

- Codex plugin install works; Hyperframes 0.9.30 renders.
- Test video: PocketLab, 21 seconds, 1920×1080, 30 fps, 1.5 MB, music +
  sound effects. Burmese hero line renders correctly.
- Hyperframes check: 0 errors, 33/33 contrast passed.
- Two fixes needed on the test machine are documented in
  `docs/06-troubleshooting.md` (low disk on `/tmp`, GSAP CDN failure).

Things **not** tested are listed honestly in `docs/07-limits.md` (Claude Code
run, Codex agent run with auth, audio-reactive visuals, Windows install).

## Links

- Upstream: https://github.com/latent-spaces/brag
- Docs: https://latent-spaces.github.io/brag
- Hosted: https://letsbrag.app
- Fork: https://github.com/mymyanmarland/brag

## License

MIT — see [LICENSE](LICENSE). /brag itself is MIT by latent-spaces.
