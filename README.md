# Gunman Contracts modding notes

Community documentation of the functions found in *Gunman Contracts Standalone*:
what they do, when the game triggers them, and which variables matter.

Static site built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/),
hosted free on GitHub Pages. No server, no database: the Markdown files in `docs/` are the data.

## Set up (once)

1. Create a GitHub **organization** for the community and a repo inside it, so the project outlives any one person's account.
2. Push this folder to the `main` branch.
3. In the repo: **Settings → Pages → Source: GitHub Actions**.
4. In `mkdocs.yml`, replace `YOUR-ORG` in `site_url` and `repo_url`.

Every merge to `main` rebuilds and publishes the site. Pull requests are only test-built.

## Add content

Copy `templates/class-template.md` to `docs/<section>/<classname>.md`. The navigation and
the home page table pick it up automatically. Details are on the site's *Contributing* page.

## Preview locally

```bash
pip install -r requirements.txt
mkdocs serve
```
