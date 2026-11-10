# Troubleshooting

ဖြေရှင်နည်း

## 1. Render refused — low disk space on /tmp

On the test machine, `/tmp` is a 512 MB tmpfs. The render refused for low
disk. Fix: point the temp and frame-cache folders at your workspace on every
Hyperframes command:

```
TMPDIR=~/workspace/brag-test/tmpdir HYPERFRAMES_EXTRACT_CACHE_DIR=~/workspace/brag-test/frames-cache npx hyperframes render --output brag-output/brag.mp4
```

## 2. GSAP CDN failed in render workers

The render workers could not load GSAP from cdn.jsdelivr.net
(ERR_TUNNEL_CONNECTION_FAILED), so timelines never registered and the render
was blocked. Fix: vendor GSAP locally — copy gsap.min.js from Hyperframes'
own node_modules into `composition/assets/vendor/gsap.min.js` and point
index.html at the local file.

## What to check before you trust a video

- `npx hyperframes check` — 0 errors (contrast included)
- Frames are readable — every line holds long enough to read
- Burmese text verified in the frames — never trust the plan alone
- Audio is present — ffprobe shows an audio stream, not silence
- Poster baked as frame 0 — so every platform shows the right thumbnail

If a render fails twice with the same error, stop. Read the error, fix the
cause, report it — don't loop.

