#!/usr/bin/env python3
"""Build the /brag guide site + docs (LIVE at brag-guide.funapp.live).

Run:  python3 build_site.py
Outputs: site/index.html, docs/*.md, README.md, assets/banner.svg,
         LICENSE, .gitignore
Burmese strings live in mm_strings.py (explicit \\uXXXX escapes only).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mm_strings import MM

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "site")
DOCS = os.path.join(ROOT, "docs")

CSS = """
:root{
  --bg:#fff6e5; --paper:#ffffff; --ink:#111111;
  --pink:#ff2e88; --pink-dk:#d6006e; --yellow:#ffd500; --cyan:#00b8d9; --red:#ff3b30;
  --mm-font:"Noto Serif Myanmar", serif;
}
@font-face{font-family:"Noto Serif Myanmar";font-style:normal;font-weight:700;font-display:swap;src:url(assets/noto-serif-myanmar-700.woff2) format("woff2")}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif;
  background:var(--bg);color:var(--ink);line-height:1.7}
::selection{background:var(--yellow);color:var(--ink)}
:focus-visible{outline:3px solid var(--cyan);outline-offset:2px}
[lang="my"],.lang-mm{font-family:var(--mm-font);font-weight:700;line-height:1.9}
a{color:var(--pink-dk);font-weight:700}
a:hover{color:var(--pink)}
.wrap{max-width:1020px;margin:0 auto;padding:0 18px}
header.top{position:sticky;top:0;z-index:20;background:var(--paper);
  border-bottom:3px solid var(--ink)}
.topbar{display:flex;align-items:center;gap:14px;padding:12px 18px;flex-wrap:wrap}
.logo{font-weight:900;font-size:22px;letter-spacing:.5px}
.logo span{color:var(--pink)}
.lang-toggle{margin-left:auto;display:flex;border:3px solid var(--ink);
  border-radius:999px;overflow:hidden;background:var(--paper)}
.lang-toggle button{background:transparent;color:var(--ink);border:0;
  padding:8px 16px;font-weight:800;cursor:pointer;font-size:14px}
.lang-toggle button.on{background:var(--yellow);color:var(--ink)}
.hero{position:relative;padding:64px 0 46px;text-align:center;overflow:hidden;
  background-color:var(--yellow);
  background-image:radial-gradient(rgba(17,17,17,.14) 1.8px, transparent 1.9px);
  background-size:20px 20px;border-bottom:3px solid var(--ink)}
.burst{position:absolute;top:24px;right:5%;width:112px;height:112px;
  display:flex;align-items:center;justify-content:center;text-align:center;
  background:var(--pink);color:#fff;font-weight:900;font-size:19px;line-height:1.1;
  transform:rotate(10deg);
  clip-path:polygon(50% 0%,61% 12%,74% 5%,79% 19%,93% 18%,92% 33%,100% 45%,92% 55%,97% 70%,84% 74%,82% 89%,68% 86%,58% 98%,47% 88%,34% 96%,26% 84%,12% 85%,11% 70%,0% 60%,6% 46%,2% 31%,15% 26%,13% 11%,28% 12%);
  filter:drop-shadow(4px 4px 0 #111)}
.kicker{display:inline-block;letter-spacing:3px;font-weight:800;color:var(--yellow);
  font-size:13px;text-transform:uppercase;background:var(--ink);
  padding:7px 16px;border-radius:999px}
.hero h1{font-size:clamp(38px,7vw,64px);line-height:1.08;margin:16px 0 10px;
  font-weight:900;text-transform:uppercase}
.hero h1 span{color:var(--pink);text-shadow:4px 4px 0 var(--ink)}
.hero p{max-width:680px;margin:0 auto;color:#222;font-size:clamp(16px,2.4vw,19px);
  font-weight:600}
.cta{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:26px}
.btn{display:inline-block;padding:13px 22px;border-radius:12px;font-weight:900;
  text-decoration:none;font-size:15px;border:3px solid var(--ink);
  box-shadow:5px 5px 0 var(--ink);transition:transform .12s,box-shadow .12s}
.btn:hover{transform:translate(-2px,-2px);box-shadow:7px 7px 0 var(--ink)}
.btn:active{transform:translate(3px,3px);box-shadow:2px 2px 0 var(--ink)}
.btn-gold{background:var(--pink);color:#fff}
.btn-ghost{background:#fff;color:var(--ink)}
.stats{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-top:28px}
.stats span{background:#fff;border:3px solid var(--ink);border-radius:999px;
  padding:8px 14px;font-weight:800;font-size:14px;box-shadow:3px 3px 0 var(--ink)}
.stats span:nth-child(odd){transform:rotate(-1.5deg)}
.stats span:nth-child(even){transform:rotate(1.5deg)}
.dots{height:24px;background:var(--pink);
  background-image:radial-gradient(#111 2.2px, transparent 2.3px);
  background-size:16px 16px;border-bottom:3px solid var(--ink)}
.tabs{display:flex;gap:10px;flex-wrap:wrap;margin:26px 0 8px}
.tabs button{border:3px solid var(--ink);background:#fff;color:var(--ink);
  padding:10px 14px;border-radius:999px;font-weight:800;cursor:pointer;font-size:14px;
  box-shadow:3px 3px 0 var(--ink);transition:transform .12s,box-shadow .12s}
.tabs button:hover{transform:translate(-2px,-2px);box-shadow:5px 5px 0 var(--ink)}
.tabs button.on{background:var(--pink);color:#fff}
.panel{display:none;scroll-margin-top:96px;background:var(--paper);
  border:3px solid var(--ink);border-radius:18px;padding:26px;margin:14px 0 40px;
  box-shadow:8px 8px 0 var(--ink)}
.panel.on{display:block}
.panel h2{margin:0 0 6px;font-size:28px;font-weight:900}
.panel h3{margin:22px 0 6px;color:var(--pink-dk);font-weight:900}
.lede{color:#444;margin:0 0 10px}
ul{margin:8px 0;padding-left:22px}
li{margin:6px 0}
code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:.92em;
  background:#fff3ad;border:2px solid var(--ink);border-radius:6px;padding:2px 6px;
  color:var(--ink)}
pre{background:#111;border:3px solid var(--ink);border-radius:12px;color:#fff;
  padding:14px 16px;overflow-x:auto;white-space:pre-wrap;word-break:break-word;
  box-shadow:6px 6px 0 var(--pink)}
pre code{background:none;border:0;padding:0;color:#ffe45e}
.copybox{position:relative;margin:14px 0}
.copybtn{position:absolute;top:8px;right:8px;background:var(--pink);color:#fff;
  border:3px solid var(--ink);border-radius:10px;padding:7px 12px;font-weight:800;
  cursor:pointer;box-shadow:3px 3px 0 var(--ink)}
.copybtn.big{position:static;width:100%;padding:13px;font-size:15px;margin-bottom:10px}
.callout{border:3px solid var(--ink);background:#fff3ad;
  padding:12px 16px;border-radius:12px;margin:16px 0;box-shadow:5px 5px 0 var(--ink)}
.callout.warn{border-color:var(--ink);background:#ffe3e0}
.check{list-style:none;padding-left:0}
.check li::before{content:"\\2713  ";color:var(--pink-dk);font-weight:900}
video{width:100%;border-radius:14px;border:3px solid var(--ink);display:block;
  box-shadow:8px 8px 0 var(--pink)}
figure{margin:18px 0}
figcaption{color:#555;font-size:14px;margin-top:8px;text-align:center}
table{width:100%;border-collapse:collapse;margin:12px 0}
td,th{padding:9px 10px;border-bottom:2px solid var(--ink);text-align:left;
  font-size:15px;vertical-align:top}
footer{border-top:3px solid var(--ink);background:#fff;padding:26px 0 40px;
  color:#444;font-size:14px}
.lang-mm{display:none}
body.mm .lang-en{display:none}
body.mm .lang-mm{display:block}
body.mm .lang-mm.inline{display:inline}
@media(max-width:640px){.panel{padding:18px}.hero{padding:44px 0 30px}.burst{display:none}}
"""

JS = """
function showTab(id, go){
  document.querySelectorAll('.panel').forEach(function(p){p.classList.remove('on')});
  document.querySelectorAll('.tabs button').forEach(function(b){b.classList.remove('on')});
  var el=document.getElementById(id); if(el){el.classList.add('on');}
  var btn=document.querySelector('[data-tab="'+id+'"]'); if(btn){btn.classList.add('on');}
  if(go){
    if(el && el.scrollIntoView){el.scrollIntoView({behavior:'smooth', block:'start'});}
    if(history.replaceState){history.replaceState(null,'','#'+id);}
  }
}
function setLang(l){
  document.body.classList.toggle('mm', l==='mm');
  document.querySelectorAll('.lang-toggle button').forEach(function(b){
    b.classList.toggle('on', b.dataset.lang===l);
  });
  try{localStorage.setItem('brag-guide-lang', l);}catch(e){}
}
function copyText(btn, text){
  function done(){var o=btn.textContent; btn.textContent='Copied!'; setTimeout(function(){btn.textContent=o;},1400);}
  function fb(){var ta=document.createElement('textarea'); ta.value=text;
    document.body.appendChild(ta); ta.select();
    try{document.execCommand('copy'); done();}catch(e){}
    document.body.removeChild(ta);}
  if(navigator.clipboard && navigator.clipboard.writeText){
    navigator.clipboard.writeText(text).then(done, fb);
  } else { fb(); }
}
document.addEventListener('DOMContentLoaded', function(){
  var hash=(location.hash||'#what').slice(1);
  if(!document.getElementById(hash)){hash='what';}
  showTab(hash, false);
  var saved=null; try{saved=localStorage.getItem('brag-guide-lang');}catch(e){}
  if(saved==='mm'){setLang('mm');}
  document.querySelectorAll('[data-copy]').forEach(function(btn){
    btn.addEventListener('click', function(){
      var t=document.getElementById(btn.dataset.copy);
      if(t){copyText(btn, t.innerText);}
    });
  });
});
"""

TABS = [
    ("what", "1. What is /brag?"),
    ("quick", "2. Quick start"),
    ("phase1", "3. Phase 1: Get ready"),
    ("phase2", "4. Phase 2: Ask for video"),
    ("copy", "5. Copy-paste messages"),
    ("fix", "6. Troubleshooting"),
    ("limits", "7. What it can't do"),
    ("faq", "8. FAQ"),
]


def mm_block(key_intro, bullets):
    lis = "".join("<li>%s</li>" % b for b in bullets)
    return ('<div class="lang-mm" lang="my"><p class="lede">%s</p><ul>%s</ul></div>'
            % (MM[key_intro], lis))


def section(sec_id, en_title, mm_title_key, en_html, mm_html, shared=""):
    return ('<section class="panel" id="%s">'
            '<h2><span class="lang-en">%s</span>'
            '<span class="lang-mm" lang="my">%s</span></h2>'
            '%s%s%s</section>'
            % (sec_id, en_title, MM[mm_title_key], en_html, mm_html, shared))

# ---------------------------------------------------------------- content
S1_EN = """
<div class="lang-en">
<p class="lede">/brag is an open-source agent skill that turns a project you just built
into a short, shareable launch video — music, motion, and share copy included.
One command. No video editor.</p>
<div class="callout"><strong>Made for Muse.</strong> /brag runs inside your Muse — the Muse reads your project, plans the video, and renders it. You never open a video editor; you just ask your Muse.</div>
<h3>Who made it</h3>
<p>By <strong>latent-spaces</strong> (Shunit Haviv Hakimi), MIT license.
Original repo: <a href="https://github.com/latent-spaces/brag">github.com/latent-spaces/brag</a>
(created 2026-06-16). Docs: <a href="https://latent-spaces.github.io/brag">latent-spaces.github.io/brag</a>.
A hosted version runs at <a href="https://letsbrag.app">letsbrag.app</a>
(paste a site link, get a video). A community fork lives at
<a href="https://github.com/mymyanmarland/brag">github.com/mymyanmarland/brag</a>.</p>
<h3>How it works</h3>
<ol>
<li>The agent <strong>reads your project code</strong> to understand what the app does.</li>
<li>It <strong>plans the story</strong> — the angle, the hook, the best moments to show.</li>
<li>It uses your <strong>real UI and branding</strong>, not stock filler.</li>
<li>It <strong>builds the scenes</strong> with motion, music, and sound effects.</li>
<li>It <strong>renders the video</strong> with Hyperframes — HeyGen's open-source
HTML-to-video framework.</li>
</ol>
<h3>What it's for</h3>
<p>Developers, indie hackers, and founders who built an app with a coding agent
and want a launch video fast — for X, LinkedIn, Facebook, or Discord.
Voiceover is off by default; <code>/brag --voice</code> adds Kokoro narration.
<code>/brag-slim</code> is a lean variant for Claude Opus 5.5 (no Hyperframes).</p>
<h3>What you get</h3>
<p>Everything lands in <code>brag-output/</code>:</p>
<ul>
<li><code>brag.mp4</code> — the rendered video (15–25 seconds)</li>
<li><code>brag.jpg</code> — the poster frame (also baked in as frame 0)</li>
<li><code>brag-plan.md</code> — the plan and storyboard</li>
<li><code>composition-brief.md</code> — the brief handed to Hyperframes</li>
<li><code>share-copy.txt</code> — the caption, ready to post</li>
<li><code>composition/</code> — the Hyperframes project</li>
</ul>
</div>
"""

S1_SHARED = """
<h3>Example 1 — PocketLab</h3>
<p>This 21-second video was made from a real project (PocketLab, a phone science
lab with 100 experiments) on a test machine: 1920&times;1080, 30 fps, 1.5 MB,
music + sound effects. Hyperframes check: 0 errors, 33/33 contrast passed.
The Burmese hero line renders correctly.</p>
<figure>
<video controls preload="metadata" poster="assets/brag.jpg" src="assets/brag.mp4"></video>
<figcaption>PocketLab launch video, made with /brag. Share copy:
&ldquo;Made PocketLab — a science lab in your phone. 100 experiments, in Burmese.&rdquo;</figcaption>
</figure>
<h3>Example 2 — This guide's own video</h3>
<p>This guide has its own launch video, made the same way — /brag, 21 seconds, music + sound effects. Watch it, then make one for your project.</p>
<figure>
<video controls preload="metadata" poster="assets/guide-video.jpg" src="assets/guide-video.mp4"></video>
<figcaption>The /brag Guide's own launch video, made with /brag.</figcaption>
</figure>
"""

S1_MM = mm_block("i1", [MM["w1"], MM["w2"], MM["w3"], MM["muse1"]]) + '<div class="lang-mm" lang="my"><div class="callout"><strong>%s</strong> %s</div></div>' % (MM["muse1"], MM["muse2"])

S2_EN = """
<div class="lang-en">
<p class="lede">Three steps. Install, check, run.</p>
<h3>Step 1 — Install /brag</h3>
<p><strong>Codex:</strong></p>
<div class="copybox"><button class="copybtn" data-copy="c-codex">Copy</button>
<pre id="c-codex"><code>codex plugin marketplace add latent-spaces/brag
codex plugin add brag@brag</code></pre></div>
<p><strong>Claude Code:</strong></p>
<div class="copybox"><button class="copybtn" data-copy="c-claude">Copy</button>
<pre id="c-claude"><code>/plugin marketplace add latent-spaces/brag
/plugin install brag@brag</code></pre></div>
<p><strong>Any other agent</strong> (Cursor, Copilot, Gemini CLI, opencode):</p>
<div class="copybox"><button class="copybtn" data-copy="c-other">Copy</button>
<pre id="c-other"><code>npx skills add https://github.com/latent-spaces/brag --skill brag</code></pre></div>
<p>Add <code>-g</code> to install globally (every project); drop it to scope to one project.</p>
<h3>Step 2 — Check the requirements</h3>
<ul>
<li>An agent that supports Agent Skills (Claude Code, Codex CLI, opencode, Cursor, Copilot, Gemini CLI)</li>
<li>Node.js 22+</li>
<li>FFmpeg on <code>PATH</code></li>
<li>Hyperframes CLI — check it and fetch its browser:</li>
</ul>
<div class="copybox"><button class="copybtn" data-copy="c-req">Copy</button>
<pre id="c-req"><code>npx hyperframes doctor
npx hyperframes browser ensure</code></pre></div>
<h3>Step 3 — Run it inside any project</h3>
<div class="copybox"><button class="copybtn" data-copy="c-run">Copy</button>
<pre id="c-run"><code>/brag</code></pre></div>
<p>Steer it if you like: <code>/brag --tone polished</code>,
<code>/brag --format vertical</code>, <code>/brag --voice</code>.
Your video appears in <code>brag-output/brag.mp4</code>.</p>
</div>
"""

S2_MM = mm_block("i2", [MM["q1"], MM["q2"], MM["q3"]])

S3_EN = """
<div class="lang-en">
<p class="lede">Before any real video: get the Muse ready, and prove it with a test render.</p>
<h3>Why two phases?</h3>
<p>Install problems (missing browser, low disk, blocked CDN) are much cheaper to
find on a throwaway example than on your real launch video. Phase 1 finds them
once, so Phase 2 is smooth.</p>
<h3>Phase 1 steps</h3>
<ol>
<li>Open the Muse's <strong>own chat</strong> and send it the Phase 1 message
(Section 5 — one Copy All tap).</li>
<li>The Muse installs /brag and Hyperframes <strong>on its own machine</strong>,
downloading them itself from GitHub. Nobody can push files into another
Muse's machine — each one installs it itself.</li>
<li>It <strong>proves it works</strong>: it clones the brag repo and runs /brag on
one of its bundled examples to render a short test video.</li>
<li>It runs <code>npx hyperframes check</code> in the composition and fixes every error.</li>
<li>It <strong>shows you the test video and the check result</strong>. It makes
nothing real yet — it waits for your project.</li>
</ol>
<h3>What "ready" looks like</h3>
<ul class="check">
<li>Plugin installed (Codex) or skill installed (other agents)</li>
<li><code>npx hyperframes doctor</code> passes (browser ready)</li>
<li>Test video exists, 15–25 seconds, with audio</li>
<li>Hyperframes check: 0 errors</li>
<li>Frames are readable, and any Burmese text is verified in the frames</li>
</ul>
<div class="callout"><strong>One video, one Muse at a time.</strong>
Never give the same video task to two Muses.</div>
</div>
"""

S3_MM = mm_block("i3", [MM["p1a"], MM["p1b"]])

S4_EN = """
<div class="lang-en">
<p class="lede">The Muse is ready. Now give it a project.</p>
<h3>What to send</h3>
<ul>
<li><strong>App name</strong> — e.g. PocketLab, ShwePrompt, KeyScope.</li>
<li><strong>Repo link</strong> — e.g. <code>https://github.com/&lt;you&gt;/&lt;app&gt;</code>,
or the project folder if it has no repo yet.</li>
<li><strong>What to highlight</strong> (optional) — the one feature or claim
the video must show. One line is enough.</li>
<li><strong>Tone / format</strong> (optional) — default is landscape, polished,
15–25 seconds. Say <code>vertical</code> or <code>square</code> for social feeds.</li>
</ul>
<h3>What happens next</h3>
<ol>
<li>The Muse reads the project, plans the video, and renders it.</li>
<li>It <strong>shows you the video and key frames first</strong>. Nothing is published.</li>
<li>You review it. Wrong word, wrong scene, wrong tone? Say so — it re-renders.</li>
<li>When you approve, <strong>download the mp4 and post it yourself</strong>.</li>
</ol>
<h3>Worked examples</h3>
<p><strong>PocketLab.</strong> The Phase 2 message (Section 5) with "PocketLab" + its project folder → the Muse returned a 21-second video, music + sound effects, plus the frames. Nothing was published.</p>
<p><strong>This guide.</strong> The same flow made the guide's own 21-second launch video — watch it in Section 1. Same steps, same checks, same "show first" rule.</p>
<p><strong>Your app.</strong> Replace "PocketLab" with your app name and add its repo link. The steps don't change.</p>
<div class="callout"><strong>Show first, publish later.</strong>
A draft agreed in principle is not a publish go. The video only goes public
when you say so, after you have seen it.</div>
</div>
"""

S4_MM = mm_block("i4", [MM["p2b"]]) + '<div class="lang-mm" lang="my"><h3>%s</h3><ul>%s</ul></div>' % (MM["ex"], "".join("<li>%s</li>" % MM[k] for k in ("p4a", "p4b", "p4c")))

PHASE1_MSG = """Get ready to make launch videos with /brag, the open-source skill from https://github.com/latent-spaces/brag. Install it on YOUR OWN VM now, so you are ready when I give you a project. Download everything yourself from GitHub on your machine.
codex plugin marketplace add latent-spaces/brag
codex plugin add brag@brag
npx hyperframes browser ensure
For other agents: npx skills add https://github.com/latent-spaces/brag --skill brag
Then prove it works: clone https://github.com/latent-spaces/brag and run /brag on one of its bundled examples to render a short test video.
Run npx hyperframes check in the composition and fix every error.
Show me the test video and the check result. Do not make any real project video yet. Wait until I give you an app and its repo.
If /tmp is small, set TMPDIR to a workspace folder before rendering.
If the GSAP CDN fails, vendor GSAP locally."""

PHASE2_MSG = """Make a launch video for my app with /brag.
App name: PocketLab
Repo link: https://github.com/&lt;you&gt;/&lt;app&gt;
Show me the video and frames first. Do not publish anything."""

S5_EN = """
<div class="lang-en">
<p class="lede">Two messages. One tap each — Copy All, paste into the Muse's own chat.
Replace <code>PocketLab</code> with your app name, and add its repo link.</p>
</div>
"""

S5_SHARED = """
<h3>Phase 1 — Get ready</h3>
<div class="copybox"><button class="copybtn big" data-copy="c-phase1">Copy All</button>
<pre id="c-phase1"><code>__PHASE1__</code></pre></div>
<h3>Phase 2 — Ask for your video</h3>
<div class="copybox"><button class="copybtn big" data-copy="c-phase2">Copy All</button>
<pre id="c-phase2"><code>__PHASE2__</code></pre></div>
""".replace("__PHASE1__", PHASE1_MSG).replace("__PHASE2__", PHASE2_MSG)

S5_MM = mm_block("i5", [MM["m1"], MM["m2"]])

S6_EN = """
<div class="lang-en">
<p class="lede">Two problems came up during the verified test run. Both have fixes.</p>
<h3>1. Render refused — low disk space on /tmp</h3>
<p>On the test machine, <code>/tmp</code> is a 512 MB tmpfs. The render refused
for low disk. <strong>Fix:</strong> point the temp and frame-cache folders at
your workspace on every Hyperframes command:</p>
<div class="copybox"><button class="copybtn" data-copy="c-tmp">Copy</button>
<pre id="c-tmp"><code>TMPDIR=~/workspace/brag-test/tmpdir HYPERFRAMES_EXTRACT_CACHE_DIR=~/workspace/brag-test/frames-cache npx hyperframes render --output brag-output/brag.mp4</code></pre></div>
<h3>2. GSAP CDN failed in render workers</h3>
<p>The render workers could not load GSAP from <code>cdn.jsdelivr.net</code>
(<code>ERR_TUNNEL_CONNECTION_FAILED</code>), so timelines never registered and
the render was blocked. Snapshots had worked — only the render path failed.
<strong>Fix:</strong> vendor GSAP locally — copy <code>gsap.min.js</code> from
Hyperframes' own <code>node_modules</code> into
<code>composition/assets/vendor/gsap.min.js</code> and point
<code>index.html</code> at the local file.</p>
<h3>What to check before you trust a video</h3>
<ul class="check">
<li><code>npx hyperframes check</code> — 0 errors (contrast included)</li>
<li>Frames are readable — every line holds long enough to read</li>
<li>Burmese text verified in the frames — never trust the plan alone</li>
<li>Audio is present — <code>ffprobe</code> shows an audio stream, not silence</li>
<li>Poster baked as frame 0 — so every platform shows the right thumbnail</li>
</ul>
<div class="callout warn"><strong>If a render fails twice</strong> with the same
error, stop. Read the error, fix the cause, and report it — don't loop.</div>
</div>
"""

S6_MM = mm_block("i6", [MM["tr1"], MM["tr2"]])

S7_EN = """
<div class="lang-en">
<p class="lede">Honest limits. These are untested or out of scope — the guide says so
rather than pretending otherwise.</p>
<table>
<tr><th>Thing</th><th>Status</th></tr>
<tr><td>Running /brag inside Claude Code</td><td>Untested — Claude Code was not installed on the test machine.</td></tr>
<tr><td>Running /brag inside Codex with auth</td><td>Untested — plugin install needs no auth, but the agent run needs Codex signed in.</td></tr>
<tr><td>Audio-reactive visuals</td><td>Untested — skipped in the test run. Music beat-sync was verified.</td></tr>
<tr><td>Windows install</td><td>Untested — the README says symlinks need Developer Mode / <code>git config core.symlinks true</code>.</td></tr>
<tr><td>Code-only projects</td><td>Weak videos — /brag needs real UI or copy to show. No UI, no story.</td></tr>
<tr><td>Burmese text</td><td>Verify in frames — AI tools can mis-shape Myanmar script. The test video's Burmese line was copied byte-verbatim from the project and frame-checked.</td></tr>
</table>
</div>
"""

S7_MM = mm_block("i7", [MM["u1"], MM["u2"], MM["u3"]])

S8_EN = """
<div class="lang-en">
<h3>Do I need Codex or Claude Code on my own machine?</h3>
<p>No. Ask your Muse — it installs /brag and renders on its own machine, then
shows you the video. Install it yourself only if you want to run it directly
without waiting.</p>
<h3>Can one Muse make videos for all my apps?</h3>
<p>Yes — one at a time. Give it one app, review the video, then the next.</p>
<h3>Can two Muses work on the same video?</h3>
<p>No. One video, one Muse. Two agents on one video double the work and split
the decisions.</p>
<h3>Where does the video file live?</h3>
<p>In the Muse's workspace, under <code>brag-output/brag.mp4</code>. Download it
from the chat and post it yourself.</p>
<h3>Does it cost anything?</h3>
<p>/brag and Hyperframes are free and open source. The agent run uses your AI
provider's tokens or API plan — the same cost as any other agent task.</p>
<h3>Can I use my own fork?</h3>
<p>Yes. Replace <code>latent-spaces/brag</code> with <code>mymyanmarland/brag</code>
(or your fork) in the install commands. Example fork:
<a href="https://github.com/mymyanmarland/brag">github.com/mymyanmarland/brag</a>.</p>
<h3>What is /brag-slim?</h3>
<p>The same /brag, rebuilt lean for Claude Opus 5.5 — no Hyperframes, same
creative rules. On Opus 5.5, /brag switches to /brag-slim automatically.</p>
</div>
"""

S8_MM = '<div class="lang-mm" lang="my">' + "".join("<h3>%s</h3><p>%s</p>" % (MM["fq%d" % n], MM["fa%d" % n]) for n in (1, 2, 3, 4)) + '</div>'

SECTIONS = [
    ("what", "What is /brag?", "t1", S1_EN, S1_MM, S1_SHARED),
    ("quick", "Quick start", "t2", S2_EN, S2_MM),
    ("phase1", "Phase 1: Get your Muse ready", "t3", S3_EN, S3_MM),
    ("phase2", "Phase 2: Ask for your video", "t4", S4_EN, S4_MM),
    ("copy", "Copy-paste messages", "t5", S5_EN, S5_MM, S5_SHARED),
    ("fix", "Troubleshooting", "t6", S6_EN, S6_MM),
    ("limits", "What it can't do", "t7", S7_EN, S7_MM),
    ("faq", "FAQ", "t8", S8_EN, S8_MM),
]

# ---------------------------------------------------------------- assemble
def build_html():
    tabs_html = "".join(
        '<button data-tab="%s" onclick="showTab(\'%s\', true)">%s</button>'
        % (i, i, label) for i, label in TABS)
    panels = "".join(section(*s) for s in SECTIONS)
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>/brag Guide — You built it. Now brag.</title>
<meta name="description" content="Use /brag with Muse: your AI agent turns your project into a short launch video — one command, no video editor.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800;900&display=swap" rel="stylesheet">
<style>%s</style>
</head>
<body>
<header class="top"><div class="wrap topbar">
<div class="logo">/brag<span> Guide</span></div>
<div class="lang-toggle" role="group" aria-label="Language">
<button data-lang="en" class="on" onclick="setLang('en')">English</button>
<button data-lang="mm" lang="my" onclick="setLang('mm')">\u1019\u103c\u1014\u103a\u1019\u102c</button>
</div></div></header>
<section class="hero"><div class="burst">21s<br>VIDEO!</div><div class="wrap">
<div class="kicker">/brag &times; Muse &middot; Open-source agent skill &middot; MIT</div>
<h1>You built it.<br><span>Now brag.</span></h1>
<p>Use /brag with Muse: your Muse installs it, tests it, and turns your project into a short launch video — motion, music, share copy and all. One command. No video editor.</p>
<div class="cta">
<a class="btn btn-gold" href="#quick" onclick="showTab('quick', true); return false;">Start in 3 steps</a>
<a class="btn btn-ghost" href="https://github.com/latent-spaces/brag">Upstream repo</a>
<a class="btn btn-ghost" href="https://github.com/mymyanmarland/brag">My fork</a>
</div>
<div class="stats"><span>21s test video</span><span>1920&times;1080 &middot; 30 fps</span>
<span>0 check errors</span><span>33/33 contrast</span></div>
</div></section>
<div class="dots" aria-hidden="true"></div>
<main class="wrap">
<nav class="tabs">%s</nav>
%s
</main>
<footer><div class="wrap">
<p>/brag is by <a href="https://github.com/latent-spaces/brag">latent-spaces</a>
(Shunit Haviv Hakimi), MIT. This guide is a community guide — not affiliated
with latent-spaces or HeyGen. Verified steps only; untested things are marked
as untested. <a href="https://github.com/mymyanmarland/brag">Fork</a> &middot;
<a href="https://latent-spaces.github.io/brag">Docs</a> &middot;
<a href="https://letsbrag.app">letsbrag.app</a></p>
<p><strong class="lang-en">Live:</strong><span class="lang-mm" lang="my">%s</span>
<span class="lang-en">This guide is live. Verified steps only; untested things are marked as untested.</span></p>
</div></footer>
<script>%s</script>
</body>
</html>
""" % (CSS, tabs_html, panels, MM["note"], JS)


DOC_CHAPTERS = [
    ("01-what-is-brag.md", "What is /brag?", "t1"),
    ("02-quick-start.md", "Quick start", "t2"),
    ("03-phase-1-get-ready.md", "Phase 1: Get your Muse ready", "t3"),
    ("04-phase-2-ask-for-video.md", "Phase 2: Ask for your video", "t4"),
    ("05-copy-paste-messages.md", "Copy-paste messages", "t5"),
    ("06-troubleshooting.md", "Troubleshooting", "t6"),
    ("07-limits.md", "What it can't do", "t7"),
    ("08-faq.md", "FAQ", "t8"),
]

DOC_BODIES = {
    "01-what-is-brag.md": """/brag is an open-source agent skill by latent-spaces
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
""",
    "02-quick-start.md": """## Step 1 — Install /brag

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
""",
    "03-phase-1-get-ready.md": """Before any real video: get the Muse ready, and prove it with a test
render.

1. Open the Muse's own chat and send the Phase 1 message (05-copy-paste-messages.md).
2. The Muse installs /brag and Hyperframes on its own machine, downloading
   them itself from GitHub. Nobody can push files into another Muse's
   machine — each one installs it itself.
3. It proves it works: clones the brag repo and runs /brag on one of its
   bundled examples to render a short test video.
4. It runs `npx hyperframes check` in the composition and fixes every error.
5. It shows you the test video and the check result. It makes nothing real
   yet — it waits for your project.

Ready means: plugin installed, `npx hyperframes doctor` passes, test video
exists (15-25s, with audio), Hyperframes check 0 errors, frames readable,
any Burmese text verified in the frames.

One video, one Muse at a time. Never give the same video task to two Muses.
""",
    "04-phase-2-ask-for-video.md": """Send:

- App name — e.g. PocketLab, ShwePrompt, KeyScope.
- Repo link — e.g. https://github.com/<you>/<app>, or the project folder.
- What to highlight (optional) — one line is enough.
- Tone / format (optional) — default landscape, polished, 15-25s.
  Say `vertical` or `square` for social feeds.

Then:

1. The Muse reads the project, plans the video, renders it.
2. It shows you the video and key frames first. Nothing is published.
3. You review it. Wrong word, wrong scene, wrong tone? Say so — it re-renders.
4. When you approve, download the mp4 and post it yourself.

Worked examples:

- PocketLab — the Phase 2 message with "PocketLab" + its project folder →
  the Muse returned a 21-second video, music + SFX, plus the frames.
  Nothing was published.
- This guide — the same flow made the guide's own 21-second launch video
  (see Section 1). Same steps, same checks.
- Your app — replace "PocketLab" with your app name and add its repo link.
  The steps don't change.

Show first, publish later. A draft agreed in principle is not a publish go.
""",
    "05-copy-paste-messages.md": """## Phase 1 — Get ready

```
__PHASE1__
```

## Phase 2 — Ask for your video

```
__PHASE2__
```

Replace `PocketLab` with your app name and add its repo link.
""".replace("__PHASE1__", PHASE1_MSG).replace("__PHASE2__", PHASE2_MSG),
    "06-troubleshooting.md": """## 1. Render refused — low disk space on /tmp

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
""",
    "07-limits.md": """Honest limits — untested or out of scope:

| Thing | Status |
|---|---|
| Running /brag inside Claude Code | Untested — not installed on the test machine. |
| Running /brag inside Codex with auth | Untested — plugin install needs no auth, but the agent run needs Codex signed in. |
| Audio-reactive visuals | Untested — skipped. Music beat-sync was verified. |
| Windows install | Untested — README says symlinks need Developer Mode / `git config core.symlinks true`. |
| Code-only projects | Weak videos — /brag needs real UI or copy to show. |
| Burmese text | Verify in frames — AI tools can mis-shape Myanmar script. The test video's Burmese line was copied byte-verbatim from the project and frame-checked. |
""",
    "08-faq.md": """**Do I need Codex or Claude Code on my own machine?**
No. Ask your Muse — it installs /brag and renders on its own machine, then
shows you the video.

**Can one Muse make videos for all my apps?**
Yes — one at a time.

**Can two Muses work on the same video?**
No. One video, one Muse.

**Where does the video file live?**
In the Muse's workspace, under `brag-output/brag.mp4`. Download it from the
chat and post it yourself.

**Does it cost anything?**
/brag and Hyperframes are free and open source. The agent run uses your AI
provider's tokens or API plan.

**Can I use my own fork?**
Yes. Replace `latent-spaces/brag` with your fork in the install commands.
Example: https://github.com/mymyanmarland/brag

**What is /brag-slim?**
The same /brag, rebuilt lean for Claude Opus 5.5 — no Hyperframes, same
creative rules. On Opus 5.5, /brag switches to /brag-slim automatically.
""",
}

BANNER = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" role="img" aria-label="/brag Guide — You built it. Now brag.">
<defs>
<pattern id="dots" width="18" height="18" patternUnits="userSpaceOnUse">
<circle cx="4" cy="4" r="2.2" fill="#111" opacity=".16"/>
</pattern>
<pattern id="pinkdots" width="16" height="16" patternUnits="userSpaceOnUse">
<circle cx="4" cy="4" r="2" fill="#111" opacity=".28"/>
</pattern>
</defs>
<rect width="1200" height="420" fill="#ffd500"/>
<rect width="1200" height="380" fill="url(#dots)"/>
<rect x="0" y="0" width="1200" height="420" fill="none" stroke="#111" stroke-width="6"/>
<rect x="56" y="36" width="310" height="54" rx="27" fill="#111"/>
<text x="211" y="72" text-anchor="middle" font-family="Inter,system-ui,sans-serif" font-size="30" font-weight="900" letter-spacing="2" fill="#ffd500">/brag &#215; Muse</text>
<text x="60" y="205" font-family="Inter,system-ui,sans-serif" font-size="96" font-weight="900" fill="#111">YOU BUILT IT.</text>
<text x="66" y="311" font-family="Inter,system-ui,sans-serif" font-size="96" font-weight="900" fill="#111">NOW BRAG.</text>
<text x="60" y="305" font-family="Inter,system-ui,sans-serif" font-size="96" font-weight="900" fill="#ff2e88">NOW BRAG.</text>
<text x="62" y="352" font-family="Inter,system-ui,sans-serif" font-size="24" font-weight="700" fill="#111">One command. No video editor. Your Muse does the work.</text>
<g transform="translate(1000,28)">
<g>
<animateTransform attributeName="transform" type="rotate" values="0 60 54; 7 60 54; 0 60 54" dur="6s" repeatCount="indefinite"/>
<polygon points="65,0 76,18 96,10 94,32 116,36 104,52 120,64 102,72 102,94 82,88 74,108 62,92 44,106 38,84 16,88 20,66 0,58 12,42 4,24 26,20 24,0 44,10" fill="#ff2e88" stroke="#111" stroke-width="3" stroke-linejoin="round">
<animateTransform attributeName="transform" type="scale" values="1;1.1;1" additive="sum" dur="3s" repeatCount="indefinite"/>
</polygon>
<text x="60" y="58" text-anchor="middle" font-family="Inter,system-ui,sans-serif" font-size="26" font-weight="900" fill="#111">21s</text>
<text x="60" y="84" text-anchor="middle" font-family="Inter,system-ui,sans-serif" font-size="19" font-weight="900" fill="#111">VIDEO!</text>
</g>
</g>
<g transform="translate(1000,180)">
<rect x="0" y="0" width="130" height="130" rx="22" fill="#00b8d9" stroke="#111" stroke-width="4"/>
<polygon points="48,35 100,65 48,95" fill="#fff" stroke="#111" stroke-width="4" stroke-linejoin="round">
<animateTransform attributeName="transform" type="scale" values="1;1.12;1" additive="sum" dur="2.4s" repeatCount="indefinite"/>
</polygon>
</g>
<rect x="0" y="380" width="1200" height="40" fill="#ff2e88"/>
<rect x="0" y="380" width="1200" height="40" fill="url(#pinkdots)"/>
</svg>
"""

HOW_IT_WORKS = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" role="img" aria-label="How it works — Phase 1: get your Muse ready. Phase 2: ask for your video.">
<rect x="66" y="56" width="460" height="190" fill="#111"/>
<rect x="60" y="50" width="460" height="190" fill="#fff" stroke="#111" stroke-width="3"/>
<rect x="84" y="74" width="118" height="38" rx="19" fill="#ff2e88"/>
<text x="143" y="99" text-anchor="middle" font-family="Inter,system-ui,sans-serif" font-size="17" font-weight="900" letter-spacing="1" fill="#fff">PHASE 1</text>
<text x="84" y="146" font-family="Inter,system-ui,sans-serif" font-size="27" font-weight="900" fill="#111">GET YOUR MUSE READY</text>
<text x="84" y="184" font-family="Inter,system-ui,sans-serif" font-size="19" font-weight="700" fill="#333">Install /brag + Hyperframes</text>
<text x="84" y="212" font-family="Inter,system-ui,sans-serif" font-size="19" font-weight="700" fill="#333">Test render, show video + check</text>
<line x1="540" y1="145" x2="648" y2="145" stroke="#111" stroke-width="6" stroke-dasharray="14 10">
<animate attributeName="stroke-dashoffset" values="0;-24" dur="0.8s" repeatCount="indefinite"/>
</line>
<polygon points="648,145 624,131 624,159" fill="#111"/>
<rect x="686" y="56" width="460" height="190" fill="#111"/>
<rect x="680" y="50" width="460" height="190" fill="#fff" stroke="#111" stroke-width="3"/>
<rect x="704" y="74" width="118" height="38" rx="19" fill="#00b8d9"/>
<text x="763" y="99" text-anchor="middle" font-family="Inter,system-ui,sans-serif" font-size="17" font-weight="900" letter-spacing="1" fill="#fff">PHASE 2</text>
<text x="704" y="146" font-family="Inter,system-ui,sans-serif" font-size="27" font-weight="900" fill="#111">ASK FOR YOUR VIDEO</text>
<text x="704" y="184" font-family="Inter,system-ui,sans-serif" font-size="19" font-weight="700" fill="#333">App name + repo link</text>
<text x="704" y="212" font-family="Inter,system-ui,sans-serif" font-size="19" font-weight="700" fill="#333">21s video, you review, you post</text>
</svg>
"""

README = """<p align="center"><img src="site/assets/banner.svg" width="1200" alt="/brag Guide — You built it. Now brag."></p>

<h1 align="center">/brag Guide — You built it. Now brag.</h1>

<p align="center">
  <a href="https://brag-guide.funapp.live"><img src="https://img.shields.io/badge/site-brag--guide.funapp.live-111111" alt="Live site"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-ff2e88" alt="License: MIT"></a>
  <a href="https://github.com/latent-spaces/brag"><img src="https://img.shields.io/badge/upstream-latent--spaces%2Fbrag-00b8d9" alt="Upstream"></a>
  <img src="https://img.shields.io/badge/status-live-brightgreen" alt="Status: live">
  <img src="https://img.shields.io/badge/lang-EN%20%2B%20MM-ffd500" alt="English + Burmese">
</p>

<p align="center"><strong>Use <a href="https://github.com/latent-spaces/brag">/brag</a> with Muse.</strong> Your Muse installs it, tests it, and turns your project into a short launch video — motion, music, share copy and all. One command. No video editor.<br>📖 Read the guide in English and Burmese → <a href="https://brag-guide.funapp.live">brag-guide.funapp.live</a></p>

## 🎬 Watch it — the guide's own launch video

<p align="center"><a href="https://brag-guide.funapp.live"><img src="site/assets/guide-video.jpg" width="800" alt="The /brag Guide's own 21-second launch video, made with /brag"></a></p>

<p align="center"><em>21 seconds, made with /brag — the same way this guide teaches. Click the poster to open the guide.</em></p>

## 🧭 How it works

<p align="center"><img src="site/assets/how-it-works.svg" width="1200" alt="Phase 1: get your Muse ready. Phase 2: ask for your video."></p>

1. **Get your Muse ready.** Install /brag + Hyperframes on the Muse's own machine, prove it with a test render on a bundled example, show the test video and the check result. Make nothing real yet.
2. **Give it your project.** App name + repo link. The Muse makes the video, shows video + frames first, you review, then you download and post it yourself. One video, one Muse at a time.

## 🚀 Quick start

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

## 📦 What's inside

| Path | What it is |
|---|---|
| 🌐 `site/index.html` | The guide website — 8 tabbed sections, English + Burmese toggle |
| 🎬 `site/assets/brag.mp4` | The verified PocketLab demo video (21s, 1920×1080, 30fps) |
| 🖼️ `site/assets/brag.jpg` | The demo poster frame |
| 🎬 `site/assets/guide-video.mp4` | The guide's own launch video (21s, music + sound effects) |
| 🖼️ `site/assets/guide-video.jpg` | The guide video poster frame |
| 🎨 `assets/banner.svg` | Animated Pop Art banner art |
| 🧭 `assets/how-it-works.svg` | Animated two-phase flow diagram |
| 📚 `docs/` | The same content as short Markdown chapters, one file per section |
| 🛠️ `scripts/` | Builders for the site and the Burmese strings |

## ✅ Verified, not promised

Every step in this guide was run end-to-end on a test machine on 2026-11-10:

- ✅ Codex plugin install works; Hyperframes 0.9.30 renders.
- ✅ Test video: PocketLab, 21 seconds, 1920×1080, 30 fps, 1.5 MB, music + sound effects. Burmese hero line renders correctly.
- ✅ Hyperframes check: 0 errors, 33/33 contrast passed.
- ✅ Two fixes needed on the test machine are documented in `docs/06-troubleshooting.md` (low disk on `/tmp`, GSAP CDN failure).

Things **not** tested are listed honestly in `docs/07-limits.md` (Claude Code run, Codex agent run with auth, audio-reactive visuals, Windows install).

## 🔗 Links

- 🌐 Live guide: https://brag-guide.funapp.live
- ⬆️ Upstream: https://github.com/latent-spaces/brag
- 📖 Docs: https://latent-spaces.github.io/brag
- 🎬 Hosted: https://letsbrag.app
- 🍴 Fork: https://github.com/mymyanmarland/brag

## 📄 License

MIT — see [LICENSE](LICENSE). /brag itself is MIT by latent-spaces.
"""

LICENSE = """MIT License

Copyright (c) 2026 /brag Guide contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

GITIGNORE = """node_modules/
.brag/
brag-output/
*.mp4.bak
.DS_Store
"""


def main():
    os.makedirs(SITE, exist_ok=True)
    os.makedirs(DOCS, exist_ok=True)
    os.makedirs(os.path.join(ROOT, "assets"), exist_ok=True)
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as f:
        f.write(build_html())
    for fname, title, mmkey in DOC_CHAPTERS:
        body = DOC_BODIES[fname]
        with open(os.path.join(DOCS, fname), "w", encoding="utf-8") as f:
            f.write("# %s\n\n%s\n\n%s\n" % (title, MM[mmkey], body))
    with open(os.path.join(ROOT, "README.md"), "w", encoding="utf-8") as f:
        f.write(README)
    with open(os.path.join(ROOT, "assets", "banner.svg"), "w", encoding="utf-8") as f:
        f.write(BANNER)
    with open(os.path.join(SITE, "assets", "banner.svg"), "w", encoding="utf-8") as f:
        f.write(BANNER)
    with open(os.path.join(ROOT, "assets", "how-it-works.svg"), "w", encoding="utf-8") as f:
        f.write(HOW_IT_WORKS)
    with open(os.path.join(SITE, "assets", "how-it-works.svg"), "w", encoding="utf-8") as f:
        f.write(HOW_IT_WORKS)
    with open(os.path.join(ROOT, "LICENSE"), "w", encoding="utf-8") as f:
        f.write(LICENSE)
    with open(os.path.join(ROOT, ".gitignore"), "w", encoding="utf-8") as f:
        f.write(GITIGNORE)
    print("built: site/index.html, docs/*.md, README.md, banner.svg, how-it-works.svg, LICENSE, .gitignore")


if __name__ == "__main__":
    main()
