# Contributing

Found a function that isn't listed? Add it. A few lines are enough.

## Add or change a page

1. Click the pencil icon on any page to edit it on GitHub, or use **Add file** in the repo to create a new page.
2. New class: pick the section folder under `docs/` (for example `player` or `weapons`) or create a new one. The folder name becomes the section name.
3. Start from the template below and save it as `docs/<section>/<classname>.md`.
4. Open a pull request. The site rebuilds after it is merged.

The home page table and the navigation update on their own. There is nothing else to edit.

## Conventions

- One page per game class, one `###` heading per function.
- Keep it short: one line for when it triggers, one for what we do with it.
- Keep **parameters** and **variables** apart. A parameter is declared in the function's own signature (`HurtPlayer(... ANBBasicNPC attacker)`) — document it in that function's own "Parameters" line. A variable is a field read off the object itself (`__instance.health`) — that goes in the class-wide "Tested class variables" table. Types are what you see in the code, so correct them if you know better.
- In a Harmony patch, `__instance` is the object the function ran on. Write the class's own field name (`health`), not `__instance.health`. `__result` is the value the function returns.
- Unsure about something? Say so in the text. A marked guess beats a wrong fact.

## Template

```markdown
--8<-- "templates/class-template.md"
```

## Preview locally (optional)

```bash
pip install -r requirements.txt
mkdocs serve
```
