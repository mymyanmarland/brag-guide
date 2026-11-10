# Quick start

စတင်နည်း

## Step 1 — Install /brag

Codex:
```
codex plugin marketplace add latent-spaces/brag
codex plugin add brag@brag
```

Claude Code:
```
/plugin marketplace add latent-spaces/brag
/plugin install brag@brag
```

Any other agent (Cursor, Copilot, Gemini CLI, opencode):
```
npx skills add https://github.com/latent-spaces/brag --skill brag
```
Add `-g` to install globally; drop it to scope to one project.

## Step 2 — Check the requirements

- An agent that supports Agent Skills (Claude Code, Codex CLI, opencode,
  Cursor, Copilot, Gemini CLI)
- Node.js 22+
- FFmpeg on PATH
- Hyperframes CLI:
```
npx hyperframes doctor
npx hyperframes browser ensure
```

## Step 3 — Run it inside any project

```
/brag
```

Steer it: `/brag --tone polished`, `/brag --format vertical`,
`/brag --voice`. Video appears in `brag-output/brag.mp4`.

