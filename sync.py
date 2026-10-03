#!/usr/bin/env python3
"""Copy ThinkPress Commons pages into a book, or build the commons site.

A book lists the pages it uses in `commons.yml` at its root:

    target_dir: chapters/appendices        # where synced pages go
    figures_dir: figures/commons           # where their images go
    vars:
      book_title: Think AI Systems
      book_folder: ais
      python_version: "3.13"
    pages:
      - page: python-installation          # pages/python-installation.md
        file: development_setup/python_installation.md   # relative to target_dir
        intro: |                           # optional book-specific note
          Labs run in the browser; install Python only to work locally.

Usage:
    python sync.py BOOK_DIR            # sync pages into a book
    python sync.py BOOK_DIR --check    # report pages that are out of date
    python sync.py --site              # write the standalone site into site/

Synced pages carry a marker comment; edit the page here, never the copy.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
FIGURES = ROOT / "figures"
MARKER = "<!-- Synced from thinkpress-commons/pages/{page}.md. Do not edit here: edit the commons page and run sync.py. -->"
PLACEHOLDER = re.compile(r"\{\{\s*([a-z_]+)\s*\}\}")
FIGURE_REF = re.compile(r"(?<![\w/.-])figures/([\w.-]+\.(?:png|jpg|jpeg|gif|svg))")
DOC_REF = re.compile(r"\{doc\}`(?:([^`<]*?)\s*<)?([a-z0-9-]+)>?`")
SITE_VARS = {"book_title": "your ThinkPress book", "book_folder": "mycourse", "python_version": "3.13"}


def page_title(page: str) -> str:
    for line in (PAGES / f"{page}.md").read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return page


def render(page: str, variables: dict, figure_prefix: str, intro: str | None = None,
           links: dict | None = None) -> tuple[str, set[str]]:
    """Return the page text with placeholders filled, figure and page links rewritten, and the marker added.

    `links` maps commons page names to doc paths in the target (relative to this page).
    Links to commons pages the target does not include become plain text: the commons
    site is for staff (not students or the public), so readers cannot follow them.
    """
    src = (PAGES / f"{page}.md").read_text()

    missing = sorted({m.group(1) for m in PLACEHOLDER.finditer(src)} - set(variables))
    if missing:
        raise SystemExit(f"{page}: no value for placeholder(s) {', '.join(missing)} in vars")
    text = PLACEHOLDER.sub(lambda m: str(variables[m.group(1)]), src)

    if links is not None:
        def relink(m):
            label, target = m.group(1), m.group(2)
            if not (PAGES / f"{target}.md").exists():
                return m.group(0)
            if target in links:
                return f"{{doc}}`{label} <{links[target]}>`" if label else f"{{doc}}`{links[target]}`"
            # Students cannot open the commons site, so readers get the title as plain text.
            return f"*{label or page_title(target)}*"
        text = DOC_REF.sub(relink, text)

    figures = set(FIGURE_REF.findall(text))
    text = FIGURE_REF.sub(lambda m: f"{figure_prefix}{m.group(1)}", text)

    lines = text.splitlines()
    h1 = next((i for i, line in enumerate(lines) if line.startswith("# ")), None)
    if h1 is None:
        raise SystemExit(f"{page}: page has no H1")
    insert = ["", MARKER.format(page=page)]
    if intro:
        insert += ["", intro.strip()]
    lines[h1 + 1:h1 + 1] = insert
    return "\n".join(lines).rstrip() + "\n", figures


def sync_book(book: Path, check: bool) -> int:
    cfg_file = book / "commons.yml"
    if not cfg_file.exists():
        raise SystemExit(f"{cfg_file} not found")
    cfg = yaml.safe_load(cfg_file.read_text())
    target = book / cfg.get("target_dir", "chapters/appendices")
    fig_dir = book / cfg.get("figures_dir", "figures/commons")
    variables = cfg.get("vars", {})
    outputs = {e["page"]: target / e["file"] for e in cfg["pages"]}
    stale = 0
    for entry in cfg["pages"]:
        out = outputs[entry["page"]]
        prefix = os.path.relpath(fig_dir, out.parent).replace(os.sep, "/") + "/"
        links = {p: os.path.splitext(os.path.relpath(o, out.parent))[0].replace(os.sep, "/") for p, o in outputs.items()}
        text, figures = render(entry["page"], variables, prefix, entry.get("intro"), links)
        current = out.read_text() if out.exists() else None
        old_figures = [n for n in sorted(figures)
                       if not (fig_dir / n).exists() or (fig_dir / n).read_bytes() != (FIGURES / n).read_bytes()]
        if current == text and not old_figures:
            continue
        stale += 1
        if check:
            print(f"out of date: {out.relative_to(book)}" + (f" (figures: {', '.join(old_figures)})" if old_figures else ""))
            continue
        out.parent.mkdir(parents=True, exist_ok=True)
        if current != text:
            out.write_text(text)
        for name in old_figures:
            fig_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(FIGURES / name, fig_dir / name)
        print(f"synced: {entry['page']} -> {out.relative_to(book)}" + (f" (figures: {', '.join(old_figures)})" if old_figures else ""))
    if not stale:
        print("all commons pages up to date")
    return 1 if (check and stale) else 0


def build_site() -> int:
    """Write the standalone site (site/) from the pages with neutral values."""
    site = ROOT / "site"
    pages_out = site / "pages"
    if pages_out.exists():
        shutil.rmtree(pages_out)
    pages_out.mkdir(parents=True)
    names = sorted(p.stem for p in PAGES.glob("*.md"))
    for name in names:
        text, figures = render(name, SITE_VARS, "../figures/")
        (pages_out / f"{name}.md").write_text(text)
    if (site / "figures").exists():
        shutil.rmtree(site / "figures")
    shutil.copytree(FIGURES, site / "figures", ignore=shutil.ignore_patterns(".gitkeep"))
    print(f"site: {len(names)} pages in {site.relative_to(ROOT)}/pages")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("book", nargs="?", type=Path)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--site", action="store_true")
    args = ap.parse_args()
    if args.site:
        return build_site()
    if not args.book:
        ap.error("give a book directory, or --site")
    return sync_book(args.book.resolve(), args.check)


if __name__ == "__main__":
    sys.exit(main())
