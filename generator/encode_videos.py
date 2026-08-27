#!/usr/bin/env python3
"""Re-encode rendered example videos into site/assets/video (small x264 + poster JPGs).
Uses PyAV (installed with Manim) — no ffmpeg binary needed.
Run from repo root: python3 generator/encode_videos.py
"""
import glob
import os

import av
from PIL import Image

SRC = "examples/media/videos/manim_examples/480p15"
DST = "site/assets/video"
os.makedirs(DST, exist_ok=True)

for src in sorted(glob.glob(f"{SRC}/*.mp4")):
    name = os.path.splitext(os.path.basename(src))[0]
    dst = f"{DST}/{name}.mp4"
    inp = av.open(src)
    v_in = inp.streams.video[0]
    out = av.open(dst, "w", options={"movflags": "faststart"})
    v_out = out.add_stream("libx264", rate=v_in.average_rate,
                           options={"preset": "veryslow", "crf": "26"})
    v_out.width, v_out.height = v_in.width, v_in.height
    v_out.pix_fmt = "yuv420p"
    poster_saved = False
    for n, frame in enumerate(inp.decode(video=0)):
        if n == 3 and not poster_saved:
            img = frame.to_image()
            img.thumbnail((640, 10000))
            img.save(f"{DST}/{name}.jpg", quality=72, optimize=True)
            poster_saved = True
        for pkt in v_out.encode(frame):
            out.mux(pkt)
    for pkt in v_out.encode():
        out.mux(pkt)
    out.close()
    inp.close()
    print(f"{name}: {os.path.getsize(src) // 1024}K -> {os.path.getsize(dst) // 1024}K")
