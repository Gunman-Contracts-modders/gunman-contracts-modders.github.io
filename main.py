"""Macros for the docs site.

class_overview() builds the class table on the home page by scanning
docs/<section>/<class>.md. Nothing has to be listed by hand: add a page
from the template and it shows up on its own.
"""
import re
from pathlib import Path

import yaml


def _split_front_matter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return (yaml.safe_load(parts[1]) or {}), parts[2]
    return {}, text


def define_env(env):
    docs = Path(env.conf["docs_dir"])

    @env.macro
    def class_overview():
        sections = {}
        for path in sorted(docs.glob("*/*.md")):
            if path.name.startswith("_"):  # _drafts are not listed
                continue
            meta, body = _split_front_matter(path.read_text(encoding="utf-8"))
            h1 = re.search(r"^# (.+)$", body, re.M)
            name = h1.group(1).strip() if h1 else path.stem
            functions = [
                f.strip("` ")
                for f in re.findall(r"^### (.+)$", body, re.M)
            ]
            section = path.parent.name.replace("-", " ").replace("_", " ").title()
            sections.setdefault(section, []).append(
                (name, path.relative_to(docs).as_posix(), functions,
                 meta.get("description", ""))
            )

        out = []
        for section in sorted(sections):
            out.append(f"## {section}\n")
            out.append("| Class | Functions | What it is |")
            out.append("|---|---|---|")
            for name, link, functions, desc in sorted(sections[section]):
                fns = ", ".join(f"`{f}`" for f in functions) or "–"
                out.append(f"| [{name}]({link}) | {fns} | {desc} |")
            out.append("")
        return "\n".join(out)
