#!/usr/bin/env python3
"""Build the three hand-over forms of this context pack, so any web model can read it.

  py -3 -X utf8 build_pack.py

Writes (all committed except the zip):
  ALL_IN_ONE.md        every text file concatenated + a table of raw image URLs (paste or upload ONE file)
  LINKS.md             raw URL of every file (models that fetch URLs read raw.githubusercontent.com best)
  docs/index.html      the same content as one web page with the images inline (served by GitHub Pages)
  dist/arcanum2-argon-pack.zip   everything for manual upload (local; also attached to the GitHub release)
Exit 1 if a referenced sample image is missing.
"""
from __future__ import annotations

import html
import pathlib
import re
import shutil
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent
OWNER_REPO = "AndriiEagle/arcanum2-argon-context"
BRANCH = "master"
RAW = f"https://raw.githubusercontent.com/{OWNER_REPO}/{BRANCH}/"
PAGES = f"https://{OWNER_REPO.split('/')[0].lower()}.github.io/{OWNER_REPO.split('/')[1]}/"
TEXTS = ["WORLD_BIBLE.md", "ART_BIBLE.md", "SPEC_CH1_v0.md", "prompts/README.md",
         "prompts/PROMPT_1_visual_repair_director.md", "prompts/PROMPT_2_hyperadaptive_graph.md",
         "prompts/PROMPT_3_mechanic_code_with_tests.md"]


def md_to_html(md: str) -> str:
    out, in_code, in_table = [], False, False
    for line in md.splitlines():
        if in_table and not line.startswith("|"):
            out.append("</table>")
            in_table = False
        if line.startswith("```"):
            out.append("</pre>" if in_code else "<pre>")
            in_code = not in_code
            continue
        if in_code:
            out.append(html.escape(line))
            continue
        e = html.escape(line)
        e = re.sub(r"`([^`]+)`", r"<code>\1</code>", e)
        e = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", e)
        m = re.match(r"^(#{1,4}) (.*)", e)
        if m:
            n = len(m.group(1)) + 1
            out.append(f"<h{n}>{m.group(2)}</h{n}>")
        elif e.startswith("|"):
            cells = [c.strip() for c in e.strip("|").split("|")]
            if all(set(c) <= set("-: ") for c in cells):
                continue
            if not in_table:
                out.append("<table>")
                in_table = True
            out.append("<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>")
        elif e.strip():
            out.append(f"<p>{e}</p>")
    if in_table:
        out.append("</table>")
    return "\n".join(out)


def main() -> int:
    samples = sorted(p for p in (ROOT / "samples").iterdir() if p.suffix.lower() in (".png", ".jpg", ".jpeg"))
    if not samples:
        print("no samples"); return 1
    texts = [(t, (ROOT / t).read_text(encoding="utf-8")) for t in TEXTS]

    # 1. ALL_IN_ONE.md
    parts = ["# Arcanum 2 — whole context in one file",
             f"Repository: https://github.com/{OWNER_REPO} · Web page: {PAGES}",
             "Read sections 1-3 first, look at the images, then answer exactly ONE prompt (sections 5-7).", ""]
    for i, (name, body) in enumerate(texts, 1):
        parts += [f"\n---\n\n## {i}. `{name}`\n", body.strip(), ""]
    parts += ["\n---\n\n## Sample frames (real 1280x720 playtest captures)\n", "| file | raw URL |", "|---|---|"]
    parts += [f"| {p.name} | {RAW}samples/{p.name} |" for p in samples]
    (ROOT / "ALL_IN_ONE.md").write_text("\n".join(parts) + "\n", encoding="utf-8")

    # 2. LINKS.md
    links = ["# Direct links (raw files; best for models that fetch URLs)", "",
             f"- One file with everything: {RAW}ALL_IN_ONE.md", f"- Web page with images: {PAGES}", ""]
    links += [f"- {t}: {RAW}{t}" for t in TEXTS]
    links += [f"- samples/{p.name}: {RAW}samples/{p.name}" for p in samples]
    (ROOT / "LINKS.md").write_text("\n".join(links) + "\n", encoding="utf-8")

    # 3. docs/index.html (GitHub Pages)
    (ROOT / "docs").mkdir(exist_ok=True)
    css = ("body{font:16px/1.5 Georgia,serif;max-width:980px;margin:24px auto;padding:0 16px;color:#222;background:#faf7f0}"
           "pre{background:#eee;padding:10px;white-space:pre-wrap}code{background:#eee;padding:0 3px}"
           "table{border-collapse:collapse;margin:8px 0}td{border:1px solid #ccc;padding:4px 8px;vertical-align:top}"
           "img{max-width:100%;border:1px solid #999;margin:6px 0}h2{border-top:2px solid #444;padding-top:14px}")
    body = [f"<!doctype html><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>Arcanum 2 context pack</title><style>{css}</style>",
            "<h1>Arcanum 2 — context pack for art and design models</h1>",
            f"<p>Everything on one page. Plain-text version: <a href='{RAW}ALL_IN_ONE.md'>ALL_IN_ONE.md</a>. "
            f"Repository: <a href='https://github.com/{OWNER_REPO}'>{OWNER_REPO}</a>.</p>"]
    for i, (name, txt) in enumerate(texts, 1):
        body.append(f"<h2>{i}. {html.escape(name)}</h2>")
        body.append(md_to_html(txt))
    body.append("<h2>Sample frames</h2>")
    for p in samples:
        shutil.copy2(p, ROOT / "docs" / p.name)
        body.append(f"<p><b>{p.name}</b><br><img src='{p.name}' alt='{p.name}' loading='lazy'></p>")
    (ROOT / "docs" / "index.html").write_text("\n".join(body), encoding="utf-8")

    # 4. zip
    (ROOT / "dist").mkdir(exist_ok=True)
    z = ROOT / "dist" / "arcanum2-argon-pack.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for name in ["README.md", "ALL_IN_ONE.md", "LINKS.md", *TEXTS]:
            zf.write(ROOT / name, name)
        for p in samples:
            zf.write(p, f"samples/{p.name}")
    print("ALL_IN_ONE.md", (ROOT / "ALL_IN_ONE.md").stat().st_size, "bytes;", len(samples), "samples;",
          "zip", round(z.stat().st_size / 1e6, 1), "MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
