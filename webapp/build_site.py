"""Build the static site GitHub Pages serves.

The hosted planner has no server, so the plan is parsed ahead of time by the same
parse_plan() the local server runs — the two can never disagree about the plan.

    site/index.html, lib/*.js, manifest, icon, .nojekyll
    site/data/plan.json     parse_plan() + the templates the browser needs
    site/data/config.json   which repository to read and write

Run locally with `python webapp/build_site.py`; CI runs the same command.
"""

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

WEBAPP = Path(__file__).resolve().parent
ROOT = WEBAPP.parent
OUT = ROOT / "site"
sys.path.insert(0, str(WEBAPP))

import server  # noqa: E402


def repo_config():
    slug = os.environ.get("GITHUB_REPOSITORY")
    if not slug:
        try:
            url = subprocess.run(["git", "remote", "get-url", "origin"], cwd=ROOT,
                                 capture_output=True, text=True, check=True).stdout.strip()
            slug = url.removesuffix(".git").split("github.com")[-1].lstrip(":/")
        except Exception:
            slug = "local/preview"
    owner, name = slug.split("/", 1)
    return {"repo": {"owner": owner, "name": name, "branch": os.environ.get("GITHUB_REF_NAME", "main")}}


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "data").mkdir(parents=True)
    (OUT / "lib").mkdir()
    plan = server.parse_plan()
    plan["templates"] = server.templates()
    (OUT / "data" / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (OUT / "data" / "config.json").write_text(json.dumps(repo_config(), indent=2), encoding="utf-8")
    for name in ("index.html", "manifest.webmanifest", "icon.svg"):
        shutil.copy2(WEBAPP / name, OUT / name)
    for js in sorted((WEBAPP / "lib").glob("*.js")):
        shutil.copy2(js, OUT / "lib" / js.name)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    size = (OUT / "data" / "plan.json").stat().st_size
    tasks = sum(len(d["tasks"]) for d in plan["days"])
    print(f"site/ built: {len(plan['phases'])} phases, {len(plan['days'])} days, {tasks} sessions, "
          f"{len(plan['topics'])} topics, {len(plan['problems'])} problems, plan.json {size // 1024} KB")


if __name__ == "__main__":
    main()
