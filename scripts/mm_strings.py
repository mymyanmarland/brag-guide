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
    "i2": "\u1021\u1006\u1004\u1037\u103a \u1043 \u1006\u1004\u1037\u103a\u1010\u100a\u103a\u1038\u104b",  # a-hsint 3 hsint-tay
    "i3": "Muse \u1000\u102d\u102f \u1021\u101b\u1004\u103a \u1015\u103c\u1004\u103a\u1015\u102b\u104b",  # Muse ko a-yin pyin-par
    "i4": "App \u1014\u102c\u1019\u100a\u103a \u1014\u1032\u1037 repo link \u1015\u1031\u1038\u1015\u102b\u104b",  # App na-myi ne repo link pay-par
    "i5": "Copy All \u1010\u1005\u103a\u1001\u103b\u1000\u103a \u1014\u103e\u102d\u1015\u103a \u1021\u1000\u102f\u1014\u103a \u1000\u1030\u1038\u101c\u102d\u102f\u1037\u101b\u1010\u101a\u103a\u104b",  # Copy All tit-chat nheit a-kun ku-lo-ya-tay
    "i6": "\u1015\u103b\u1000\u103a\u101b\u1004\u103a \u1012\u102e\u1019\u103e\u102c \u101b\u103e\u102c\u1015\u102b\u104b",  # pyet-yin di-hma sha-par
    "i7": "\u1012\u102b\u1010\u103d\u1031 \u1019\u101c\u102f\u1015\u103a\u1014\u102d\u102f\u1004\u103a\u101e\u1031\u1038\u1018\u1030\u1038\u104b",  # da-dwe ma-lote-nite-thay-bu
    "i8": "\u1019\u1031\u1038\u1001\u103d\u1014\u103a \u1014\u1032\u1037 \u1021\u1016\u103c\u1031\u104b",  # may-khwan ne a-hpyay
    # what-is bullets
    "w1": "Music, motion, SFX \u1015\u102b\u1010\u101a\u103a\u104b Video editor \u1019\u101c\u102d\u102f\u1018\u1030\u1038\u104b",  # ... pa-tay. Video editor ma-lo-bu
    "w2": "Agent \u1000 Project \u1000\u102d\u102f \u1016\u1010\u103a\u1010\u101a\u103a\u104b Story \u1005\u102e\u1005\u1009\u103a\u1010\u101a\u103a\u104b \u1010\u1000\u101a\u1037\u103a UI \u1000\u102d\u102f \u101e\u102f\u1036\u1038\u1010\u101a\u103a\u104b",  # Agent ka Project ko hpat-tay. Story si-sin-tay. Ta-kay UI ko thon-tay
    "w3": "\u1017\u102e\u1012\u102e\u101a\u102d\u102f \u1041\u1045\u2013\u1042\u1045 seconds\u104b",  # video 15-25 seconds
    # quick-start bullets
    "q1": "Install \u101c\u102f\u1015\u103a\u1015\u102b\u104b",
    "q2": "\u1005\u1019\u103a\u1038\u101e\u1015\u103a\u1015\u1031\u1038\u1015\u102b\u104b",  # sa-tin-pay-par (test + give)
    "q3": "Video \u1011\u102f\u1010\u103a\u1015\u102b\u104b",  # video htote-par
    # phase bullets
    "p1a": "Project \u1000\u102d\u102f \u1021\u101b\u1004\u103a \u1016\u1010\u103a\u1015\u102b\u104b",  # Project ko a-yin hpat-par
    "p1b": "Test video \u1000\u102d\u102f \u1015\u103c\u1015\u102b\u104b \u1015\u1031\u1038\u1015\u102b\u104b",  # Test video ko pya-par. pay-par
    "p2a": "App \u1014\u102c\u1019\u100a\u103a \u1014\u1032\u1037 repo link \u1015\u1031\u1038\u1015\u102b\u104b",
    "p2b": "Video \u1000\u102d\u102f \u1021\u101b\u1004\u103a \u1015\u103c\u1015\u102b\u104b",  # Video ko a-yin pya-par
    # troubleshooting
    "tr1": "/tmp \u1014\u1031\u101b\u102c \u1014\u100a\u103a\u1038\u104b TMPDIR \u1000\u102d\u102f \u1015\u103c\u1031\u102c\u1004\u103a\u1015\u1031\u1038\u1015\u102b\u104b",  # /tmp ne-ya nay. TMPDIR ko pyaw-pay-par
    "tr2": "GSAP CDN \u1019\u101b\u1015\u102b\u104b GSAP \u1000\u102d\u102f copy \u101c\u102f\u1015\u103a\u1015\u102b\u104b",  # GSAP CDN ma-ya-par. GSAP ko copy lote-par
    # misc UI
    "copy_all": "Copy All",
    "copied": "Copied!",
    "note": "\u1012\u102b\u1000 draft \u1015\u102b\u104b Publish \u1019\u101c\u102f\u1015\u103a\u1015\u102b\u1014\u1032\u1037\u104b",  # da-ka draft par. Publish ma-lote-par-ne. (footer draft warning)
}
