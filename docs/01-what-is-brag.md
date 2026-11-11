# What is /brag?

/brag ဆိုတာ ဘာလဲ

/brag is an open-source agent skill by latent-spaces
(Shunit Haviv Hakimi), MIT license. Repo: https://github.com/latent-spaces/brag
(created 2026-06-16). Docs: https://latent-spaces.github.io/brag.
Hosted: https://letsbrag.app. Fork: https://github.com/mymyanmarland/brag.

This guide is for using /brag with Muse. /brag runs inside your Muse: the Muse
reads the project, plans the video, and renders it. One video, one Muse at a time.

It turns a project you just built into a short (15-25s) launch video with
motion, music, SFX and share copy, powered by Hyperframes (HeyGen's
open-source HTML-to-video framework). The agent reads the project code, plans
the story, picks the best moments, uses the real UI/branding, builds scenes,
adds motion and audio, renders the video. No video editor needed.

Voiceover is off by default; `/brag --voice` enables Kokoro narration.
/brag-slim is a lean variant for Claude Opus 5.5 (no Hyperframes).

Output goes to `brag-output/`: brag.mp4, brag.jpg poster, brag-plan.md,
composition-brief.md, share-copy.txt, composition/.

Example: PocketLab (a phone science lab, 100 experiments). Test video: 21s,
1920x1080, 30fps, 1.5 MB, music + SFX. Hyperframes check: 0 errors, 33/33
contrast. Burmese hero line renders correctly. Share copy: "Made PocketLab —
a science lab in your phone. 100 experiments, in Burmese."

