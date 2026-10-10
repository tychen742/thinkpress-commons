# ThinkPress Commons

Shared reference pages for ThinkPress books: development tooling, environment setup, and other appendix material that several books need. This is not a book. Each book copies the pages it needs into its own appendices at build time, so every book stays complete on its own and readers never leave their book.

## Layout

- `pages/`: canonical pages (Jupyter notebooks or MyST Markdown), written to be book-neutral.
- `figures/`: images the pages use.
- `sync.py`: copies the pages a book lists in its `commons.yml` into the book, fills in its values (`{{book_title}}`, `{{book_folder}}`, `{{python_version}}`), copies the figures, and marks each copy as synced. `--site` builds the standalone site.
- `site/`: the standalone site (Jupyter Book): cover page, table of contents, and config. `site/pages` and `site/figures` are generated.

## Rules

- A page here is the single source. Fix it here, then re-sync the books; never edit a synced copy inside a book.
- Keep pages book-neutral. Language-specific commands, course rules, and chapter cross-references belong in the book's wrapper, not here.
- Each book declares the pages it uses in `commons.yml` at its root. A short book-owned wrapper page (for example "Development Setup") introduces them, and the synced pages sit under it in the book's `_toc.yml`.
- Model names, prices, and provider details stay in each book's model-access appendix.

## Scope

Commons holds only pages that are the same across books. Most appendices stay in their books (decided 2026-10-03):

- **In commons (planned first pages):** command-line fundamentals, editing tools, introductory REPL concepts, Python installation, virtual environments, Jupyter Notebook, Git basics, model access and API keys.
- **Stays in each book that needs it:** language toolchains and language-specific setup (C compiler, .NET, language extensions and REPL commands); advanced Linux/shell administration; course logistics (VMs, servers); cheat sheets; capstones and final projects; any other book-specific appendix.

Books letter all appendices A, B, C, … in `_toc.yml` order, mixing commons pages with their own. Commons pages never mention an appendix letter.

## Versions

All books share one Jupyter Book version and one Python and Jupyter version (book-authoring skill, Toolchain version rule). Commons setup pages name those versions; when the standard changes, update the pages and every book together.

## Usage

```bash
.venv/bin/python sync.py ~/workspace/ais           # sync pages into a book
.venv/bin/python sync.py ~/workspace/ais --check   # list out-of-date copies
.venv/bin/python sync.py --site && .venv/bin/jupyter-book build site   # build the site
```

Set up the environment once with `python3.13 -m venv .venv && .venv/bin/pip install -r requirements.txt`.

## Site Deployment

Pushing to `main` builds the site in GitHub Actions. Deployment runs once the GitHub environment `commons` has the `DEPLOY_KEY` secret and the `DEPLOY_HOST` and `DEPLOY_USER` variables and `DEPLOY_PATH=/srv/thinkpress/books/commons` (Press production layout). The site is for staff, not students or the public: Press serves it at commons.thinkpress.org with `"access": "staff"` (TAs, instructors, editors, authors, admins) (`press/books/settings.py`, `press/deploy/apache/commons.thinkpress.org*.conf`). Students read the guides as synced copies inside their books.

## Status

Created 2026-10-03. Page inventory across books in progress; the first pages will come from the best existing version of each duplicated appendix.

## Shared Fundamentals (2026-10-10)

Command-line, editor, and REPL fundamentals are canonical Commons references.
Books retain guided setup, language-specific installation/launch commands, and
their first-program lessons. CSCS Section 1.2 uses these references without
moving its C# setup or Section 1.3 console application out of the chapter.
