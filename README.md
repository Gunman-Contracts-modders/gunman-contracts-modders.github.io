# Gunman Contracts modding notes

Community documentation of the functions found in *Gunman Contracts Standalone*:
what they do, when the game triggers them, and which variables matter.

Static site built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/),
hosted free on GitHub Pages. No server, no database: the Markdown files in `docs/` are the data.

Live at: https://gunman-contract-modders.github.io/

## Set up (once)

The organization is **Gunman-Contract-modders**. GitHub serves a repo named exactly
`<organization>.github.io` at the root address, without a repo name at the end.

1. In the organization, create a **public** repo named `gunman-contract-modders.github.io`.
2. Push this folder to its `main` branch.
3. In the repo: **Settings → Pages → Source: GitHub Actions**.
4. Wait for the first workflow run (Actions tab). The site is then live at https://gunman-contract-modders.github.io/.

Every merge to `main` rebuilds and publishes the site. Pull requests are only test-built.

Already created the repo under another name? Rename it under **Settings → General**. GitHub
redirects the old address, and nothing in this project needs to change.

## Add content

Copy `templates/class-template.md` to `docs/<section>/<classname>.md`. The navigation and
the home page table pick it up automatically. Details are on the site's *Contributing* page.

## Preview locally

```bash
pip install -r requirements.txt
mkdocs serve
```

## Fonts

IBM Plex Sans, IBM Plex Mono and Barlow Condensed are stored in `docs/fonts` (SIL Open Font
License, licenses included), so visitors' browsers never contact a font server.
