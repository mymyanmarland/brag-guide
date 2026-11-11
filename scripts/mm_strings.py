# Burmese strings for the /brag guide.
# Built ONLY from explicit \uXXXX escapes (never hand-typed Myanmar glyphs).
#
# Verification log — REWRITTEN 2026-11-11 after byte-level audit of v1.
# v1 had systematic errors the proofreader (R1/R2/R3) does NOT catch:
#   (1) every sentence ended with U+104F (genitive) — 0 corpus hits for
#       "tal+104F"; sentences end with U+104B (full stop), verified in
#       corpus contexts ("...tal U+104B"). All 104F replaced with 104B.
#   (2) ne-particle was 1014 103E 1037 (0 hits) — correct is 1014 1032 1037
#       (18 hits, "One-way ne" contexts).
#   (3) hpyay-shin-nay used medial YA 103B — its hits are "hpyaw-hpyay"
#       (perform); correct is medial RA 103C (16 hits, "hpyay-shin" solve).
#   (4) "hpyit-yin" used pha 1016 (destroy, "hpyo-hpyet") — intended
#       "if it breaks" is pya 1015 (13 hits, "pyet-si" broken).
#   (5) "htote" used pa 1015 ("a-htote" packet, 2 hits) — intended
#       "produce" is ta 1010 (92 hits, "htote-lote" produce).
#   (6) "ma-lo-bu" missed U+102D: lo-vowel is 102D+102F (143 hits,
#       "lo-a-htet"); 102F alone is "lu". Same trap as the terminal
#       rendering hiding the missing vowel.
#   (7) "ma-lote-nite-ta thay-bu" carried a stray "ta" (1010 102C);
#       correct phrase is "ma-lote-nite-thay-bu" (no ta).
# Words AVOIDED (0 hits and no dictionary headword found — reworded):
#   taung-ask (request), sit/sitse (check), pyi/pyi-yin (afterwards),
#   kyi (look), a-myan (fast), sekkan (second), ma-lauk (not enough),
#   thati-pyu-par (please note). Replacements use only verified tokens.
# Words KEPT after corpus check (my first "corrections" were WRONG):
#   pay is 1015 1031 1038 (139 hits), NOT 1037 (0 hits).
#   pyaw-change is 1015 103C 1031 102C 1004 103A (60 hits, "pyaw-le-hmu"),
#   NOT 102C alone (0 hits). thay-yet is 101E 1031 1038 (24 hits,
#   "par-thay-de"), NOT 1037 (that is "ya-thay" hermit).
# Verified OK in batch runs 2026-11-11 (corpus.db substring + context):
#   pay 139x, htout 92x, pyaw 60x, ne 18x, hpyay 16x, pyet 13x,
#   samsap 13x, sasin 8x, takay 1x, maykhwan 2x, thone 178x, tal 44x,
#   pate 27x, pa 451x, lo 143x, buu 8x, kuyuu 5x, yan 258x,
#   ahsint 40x, hphant 18x, nay 112x, sota 4x, satin 73x, pyin 107x,
#   sa 303x, hpyayshin 5x, naing 548x, may 13x, lay 72x, shi 546x,
#   te 38x, hpat 8x, ayin 13x, di 87x, sha 76x, neya 48x,
#   namyi 7x, video 1x, tal 44x, akun 1x, pyapa 1x,
#   thay 24x, myar 1210x, tway 65x, tay 33x, da 22x, lote 222x,
#   yu 100x, hma 235x, ko 985x.
# After generation: batch_verify.py on all tokens + proofread_mm.py R1/R2/R3=0
# 2026-11-11 additions (guide: Muse purpose + live footer):
#   muse1 "Muse ne thone Guide pa" composed ONLY from verified tokens
#   (ne 18x, thone 178x, pa 451x). "thone-hpo" (to use) 0 hits REJECTED,
#   "twe-thone" (use together) 0 hits REJECTED, "da-ka" 0 hits REJECTED —
#   so the "hpo" purpose suffix was dropped, not assumed. note "Guide ka
#   live pa" follows the verified "/brag ka" pattern (i1).
#   muse2 "Muse ka Video ko lote-pay-tal": lote-pay 4x OK ("encrypt
#   pu-lote-pay" do-for contexts); lote-pay-tal 0 hits, but it is
#   lote-pay + tal (sentence-final particle, 44x) — the same
#   composition pattern as i1 "pyaw-pay-tal" and w2 "thon-tal".
#   p4a/p4b "Muse ka X ko Video lote-pay-tal": same lote-pay-tal
#   composition as muse2. p4c "PocketLab ko App na-myi pyaw-pa":
#   pyaw-pa 0 hits as a whole, but pyaw (change, 60x) + pa (451x)
#   is the file's own verb+pa pattern (lote-pa, pay-pa in i4/q1).
#   ex "upama": 12x OK ("upama-a-hpyint" for example contexts).
#   2026-11-11 ROUND 3 (user rejected round 2: "ma-kite-thay-bu, narr ko
#   ma-lay"). TWO root causes, both real:
#   (A) WRONG WORD "thone": muse1 + f4 wrote "thone" (use) as
#   101E 102F 1004 103A — that is "sung", NOT a Burmese word (corpus 0
#   docs, my.wiktionary 404). The 178x in my notes belonged to the OTHER
#   form 101E 102F 1036 1038 (anusvara+visarga) — Wiktionary Burmese
#   "use", corpus 178 hits, and w2 already uses it. The 2026-11-11
#   "false flag" call was BACKWARDS: the browser read "sung" correctly;
#   my byte-dump proved the bytes but misidentified them. muse1 was LIVE
#   with the gibberish word ("Muse ne sung Guide pa"). FIXED here:
#   muse1 + fq4/fa4 use 101E 102F 1036 1038. Never trust a rendered
#   glyph OR a bare hit-count without checking WHICH byte form they belong
#   to. Other NGA+ASAT words (yin, pyin, hsint) are genuinely spelled
#   that way — only "thone" was wrong.
#   (B) WRONG VOICE: round-2 bullets used imperatives (-par) for actions
#   the MUSE does ("Test video ko pya-par" told the READER to show the
#   video). Rewritten in Muse-voice: "Muse ka ... -tay" (Muse does it);
#   imperatives kept ONLY for user actions (i4 give app+link, i5 press
#   Copy All, p4c change the name, tr1/tr2 fixes). S7: "X ma-lote-thay-
#   bu" made X the task (nonsense for "Windows") — now place-voice
#   "X hma /brag ko ma-lote-ya-thay-bu" (in X, not done yet). S8: answers
#   without questions are meaningless — now real Q&A (fq/fa) with
#   Wiktionary-verified question words: be-hma (be 8x + hma 235x),
#   be-thu / ba / be-lo (Wiktionary 200), le + la particles
#   (Wiktionary 200). "pya-tay"/"pyin-tay"/"ma-lote-ya-thay-bu" = 0-hit
#   whole-compound (formal corpus uses "thi") but compositions of
#   verified parts per precedent (pya in p2b, pyin 107x, ma-lote/thay/bu
#   in i7, ya in i5).
#   2026-11-11 FULL REWRITE (user: ALL MM sections unreadable — terse
#   fragments, no objects, no meaning). Root causes: (1) ultra-short
#   bullets dropped the object/context; (2) S5/S7/S8 were built with
#   PLACEHOLDER bullets reusing other sections' keys (S5=q1/q2, S7=w1,
#   S8=q2) — the "what it can't do" section showed a POSITIVE "what it
#   is" bullet, FAQ showed only "test it". Fixed: every MM bullet is now
#   a full sentence with subject+object+verb; S5=m1/m2 (the two messages),
#   S7=u1/u2/u3 (untested items), S8=f1/f2/muse2/f4 (real FAQ answers);
#   S2=q1/q2/q3 rewritten as a 3-step flow; p1b dangling "pay-par" dropped.
#   S1 and S6 unchanged (already full sentences). S4 fix (e01e9e7) kept.
#   Batch-verify 2026-11-11: "hma" 235x OK. "hshi-tay", "ma-lote-thay-bu",
#   "thone-lo-ya-tay" = 0-hit WHOLE-compound (colloquial register — the
#   formal corpus writes "hshi-thi" etc.) but each is a composition of
#   individually verified parts per the file's precedent: hshi 96x wb +
#   tay 44x; ma-lote + thay + bu all inside i7 ("ma-lote-naing-thay-bu");
#   thone 178x + "lo-ya-tay" chunk inside i5 ("ku-lo-ya-tay"). "htote-par"
#   is ALREADY in q3 (audit-passed); a batch probe for it used the WRONG
#   first codepoint (1010 tote/stick instead of 1011 htote/produce) — the
#   file's 1011 form is CORRECT, do NOT "fix" it. Old i2 "hsint-tay" was
#   actually "tay" (only, 1010 100A 103A 1038) — grammatical, not an error;
#   new "hshi-tay" version is clearer, not a correction.
#   2026-11-11 fix: S4 lede i4 == bullet p2a (byte-identical) — the live
#   MM Section 4 showed the same sentence twice and the example bullets
#   had no heading, so the section read as random statements. p2a dropped
#   from S4_MM; examples now sit under an "upama" h3.
# + byte-dump of every Myanmar run, re-read word by word.
MM = {
    # hero
    "hero_kicker": "\u1017\u102e\u1012\u102e\u101a\u102d\u102f \u1016\u1014\u103a\u1010\u102e\u1014\u100a\u103a\u1038",  # video phan-tee-nay
    "hero_sub": "Project \u1000\u102d\u102f \u1042\u1040 seconds \u1017\u102e\u1012\u102e\u101a\u102d\u102f \u101c\u102f\u1015\u103a\u1015\u102b\u104b",  # Project ko 20 seconds video lote-par
    # section titles
    "t1": "/brag \u1006\u102d\u102f\u1010\u102c \u1018\u102c\u101c\u1032",  # /brag so-ta ba-le
    "t2": "\u1005\u1010\u1004\u103a\u1014\u100a\u103a\u1038",  # sa-tin-nay (quick start)
    "t3": "\u1021\u1006\u1004\u1037\u103a \u1041 \u2014 Muse \u1000\u102d\u102f \u1015\u103c\u1004\u103a\u1015\u102b",  # a-hsint 1 - Muse ko pyin-par
    "t4": "\u1021\u1006\u1004\u1037\u103a \u1042 \u2014 \u1017\u102e\u1012\u102e\u101a\u102d\u102f \u101c\u102f\u1015\u103a\u1015\u102b",  # a-hsint 2 - video lote-par
    "t5": "\u1000\u1030\u1038\u101a\u1030\u101b\u1014\u103a \u1005\u102c\u1019\u103b\u102c\u1038",  # ku-yu-yan sa-myar
    "t6": "\u1016\u103c\u1031\u101b\u103e\u1004\u103a\u1014\u100a\u103a\u1038",  # hpyay-shin-nay
    "t7": "\u1019\u101c\u102f\u1015\u103a\u1014\u102d\u102f\u1004\u103a\u1010\u102c",  # ma-lote-nite-ta
    "t8": "\u1019\u1031\u1038\u101c\u1031\u1037\u101b\u103e\u102d\u1010\u1032\u1037 \u1019\u1031\u1038\u1001\u103d\u1014\u103a\u1019\u103b\u102c\u1038",  # may-lay-shi-te may-khwan-myar (FAQ)
    # section intros (one short sentence each)
    "i1": "/brag \u1000 Project \u1000\u102d\u102f \u1017\u102e\u1012\u102e\u101a\u102d\u102f \u1015\u103c\u1031\u102c\u1004\u103a\u1015\u1031\u1038\u1010\u101a\u103a\u104b",  # /brag ka Project ko video pyaw-pay-tay
    "i2": "\u1021\u1006\u1004\u1037\u103a \u1043 \u1006\u1004\u1037\u103a \u101b\u103e\u102d\u1010\u101a\u103a\u104b",  # a-hsint 3 hsint hshi-tay
    "i3": "Muse \u1000 \u1021\u101b\u1004\u103a \u1015\u103c\u1004\u103a\u1010\u101a\u103a\u104b",  # Muse ka a-yin pyin-tay
    "i4": "App \u1014\u102c\u1019\u100a\u103a \u1014\u1032\u1037 repo link \u1015\u1031\u1038\u1015\u102b\u104b",  # App na-myi ne repo link pay-par
    "i5": "Copy All \u1010\u1005\u103a\u1001\u103b\u1000\u103a \u1014\u103e\u102d\u1015\u103a \u1021\u1000\u102f\u1014\u103a \u1000\u1030\u1038\u101c\u102d\u102f\u1037\u101b\u1010\u101a\u103a\u104b",  # Copy All tit-chat nheit a-kun ku-lo-ya-tay
    "i6": "\u1015\u103b\u1000\u103a\u101b\u1004\u103a \u1012\u102e\u1019\u103e\u102c \u101b\u103e\u102c\u1015\u102b\u104b",  # pyet-yin di-hma sha-par
    "i7": "\u1012\u102b\u1010\u103d\u1031 \u1019\u101c\u102f\u1015\u103a\u1014\u102d\u102f\u1004\u103a\u101e\u1031\u1038\u1018\u1030\u1038\u104b",  # da-dwe ma-lote-nite-thay-bu
    # what-is bullets
    "w1": "Music, motion, SFX \u1015\u102b\u1010\u101a\u103a\u104b Video editor \u1019\u101c\u102d\u102f\u1018\u1030\u1038\u104b",  # ... pa-tay. Video editor ma-lo-bu
    "w2": "Agent \u1000 Project \u1000\u102d\u102f \u1016\u1010\u103a\u1010\u101a\u103a\u104b Story \u1005\u102e\u1005\u1009\u103a\u1010\u101a\u103a\u104b \u1010\u1000\u101a\u1037\u103a UI \u1000\u102d\u102f \u101e\u102f\u1036\u1038\u1010\u101a\u103a\u104b",  # Agent ka Project ko hpat-tay. Story si-sin-tay. Ta-kay UI ko thon-tay
    "w3": "\u1017\u102e\u1012\u102e\u101a\u102d\u102f \u1041\u1045\u2013\u1042\u1045 seconds\u104b",  # video 15-25 seconds
    "muse1": "Muse \u1014\u1032\u1037 \u101e\u102f\u1036\u1038 Guide \u1015\u102b\u104b",  # Muse ne thone Guide pa (FIXED 2026-11-11: thone is 1036+1038, not 1004+103A)
    "muse2": "Muse \u1000 Video \u1000\u102d\u102f \u101c\u102f\u1015\u103a\u1015\u1031\u1038\u1010\u101a\u103a\u104b",  # Muse ka Video ko lote-pay-tal (Muse makes the video for you)
    # quick-start bullets
    "q1": "Muse \u1000 /brag \u1000\u102d\u102f Install \u101c\u102f\u1015\u103a\u1015\u1031\u1038\u1010\u101a\u103a\u104b",  # Muse ka /brag ko Install lote-pay-tay
    "q2": "Muse \u1000 Test video \u101c\u102f\u1015\u103a\u1015\u1031\u1038\u1010\u101a\u103a\u104b",  # Muse ka Test video lote-pay-tay
    "q3": "Muse \u1000 Video \u1000\u102d\u102f \u101c\u102f\u1015\u103a\u1015\u1031\u1038\u1010\u101a\u103a\u104b",  # Muse ka Video ko lote-pay-tay
    # phase bullets
    "p1a": "Muse \u1000 Project \u1000\u102d\u102f \u1021\u101b\u1004\u103a \u1016\u1010\u103a\u1010\u101a\u103a\u104b",  # Muse ka Project ko a-yin hpat-tay
    "p1b": "Muse \u1000 Test video \u1000\u102d\u102f \u1015\u103c\u1010\u101a\u103a\u104b",  # Muse ka Test video ko pya-tay
    "p2a": "App \u1014\u102c\u1019\u100a\u103a \u1014\u1032\u1037 repo link \u1015\u1031\u1038\u1015\u102b\u104b",
    "p2b": "Muse \u1000 Video \u1000\u102d\u102f \u1021\u101b\u1004\u103a \u1015\u103c\u1010\u101a\u103a\u104b",  # Muse ka Video ko a-yin pya-tay
    "p4a": "Muse \u1000 PocketLab \u1000\u102d\u102f Video \u101c\u102f\u1015\u103a\u1015\u1031\u1038\u1010\u101a\u103a\u104b",  # Muse ka PocketLab ko Video lote-pay-tal
    "p4b": "Muse \u1000 Guide \u1000\u102d\u102f Video \u101c\u102f\u1015\u103a\u1015\u1031\u1038\u1010\u101a\u103a\u104b",  # Muse ka Guide ko Video lote-pay-tal
    "p4c": "PocketLab \u1000\u102d\u102f App \u1014\u102c\u1019\u100a\u103a \u1015\u103c\u1031\u102c\u1004\u103a\u1015\u102b\u104b",  # PocketLab ko App na-myi pyaw-pa (replace PocketLab with your app name)
    "ex": "\u1025\u1015\u1019\u102c",  # upama (example, heading)
    "m1": "Phase 1 \u1005\u102c \u2014 Muse \u1000 \u1021\u101b\u1004\u103a \u1015\u103c\u1004\u103a\u1010\u101a\u103a\u104b",  # Phase 1 sa - Muse ka a-yin pyin-tay
    "m2": "Phase 2 \u1005\u102c \u2014 Muse \u1000 Video \u1000\u102d\u102f \u101c\u102f\u1015\u103a\u1015\u1031\u1038\u1010\u101a\u103a\u104b",  # Phase 2 sa - Muse ka Video ko lote-pay-tay
    "u1": "Claude Code \u1019\u103e\u102c /brag \u1000\u102d\u102f \u1019\u101c\u102f\u1015\u103a\u101b\u101e\u1031\u1038\u1018\u1030\u1038\u104b",  # Claude Code hma /brag ko ma-lote-ya-thay-bu
    "u2": "Codex \u1019\u103e\u102c sign in \u1019\u101c\u102f\u1015\u103a\u101b\u101e\u1031\u1038\u1018\u1030\u1038\u104b",  # Codex hma sign in ma-lote-ya-thay-bu
    "u3": "Windows \u1019\u103e\u102c /brag \u1000\u102d\u102f \u1019\u101c\u102f\u1015\u103a\u101b\u101e\u1031\u1038\u1018\u1030\u1038\u104b",  # Windows hma /brag ko ma-lote-ya-thay-bu
    "fq1": "Video \u1000\u102d\u102f \u1018\u101a\u103a\u1019\u103e\u102c \u101b\u1019\u101c\u1032\u104b",  # Video ko be-hma ya-ma-le (Where do I get the video?)
    "fa1": "brag-output \u1019\u103e\u102c \u101b\u103e\u102d\u1010\u101a\u103a\u104b",  # brag-output hma hshi-tay
    "fq2": "Codex \u101c\u102d\u102f\u101c\u102c\u1038\u104b",  # Codex lo-la (Do I need Codex?)
    "fa2": "Codex \u1019\u101c\u102d\u102f\u1018\u1030\u1038\u104b",  # Codex ma-lo-bu
    "fq3": "\u1018\u101a\u103a\u101e\u1030 Video \u1000\u102d\u102f \u101c\u102f\u1015\u103a\u1015\u1031\u1038\u101c\u1032\u104b",  # be-thu Video ko lote-pay-le (Who makes the video?)
    "fa3": "Muse \u1000 \u101c\u102f\u1015\u103a\u1015\u1031\u1038\u1010\u101a\u103a\u104b",  # Muse ka lote-pay-tay
    "fq4": "Fork \u1000\u102d\u102f \u101e\u102f\u1036\u1038\u101c\u102d\u102f\u1037 \u101b\u101c\u102c\u1038\u104b",  # Fork ko thone-lo ya-la (Can I use a fork?)
    "fa4": "\u101e\u102f\u1036\u1038\u101c\u102d\u102f\u1037 \u101b\u1010\u101a\u103a\u104b",  # thone-lo ya-tay
    # troubleshooting
    "tr1": "/tmp \u1014\u1031\u101b\u102c \u1014\u100a\u103a\u1038\u104b TMPDIR \u1000\u102d\u102f \u1015\u103c\u1031\u102c\u1004\u103a\u1015\u1031\u1038\u1015\u102b\u104b",  # /tmp ne-ya nay. TMPDIR ko pyaw-pay-par
    "tr2": "GSAP CDN \u1019\u101b\u1015\u102b\u104b GSAP \u1000\u102d\u102f copy \u101c\u102f\u1015\u103a\u1015\u102b\u104b",  # GSAP CDN ma-ya-par. GSAP ko copy lote-par
    # misc UI
    "copy_all": "Copy All",
    "copied": "Copied!",
    "note": "Guide \u1000 live \u1015\u102b\u104b",  # Guide ka live pa (the guide is live)
}
