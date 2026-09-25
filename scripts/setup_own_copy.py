"""Make this repo your own: clear the previous owner's data, create your GitHub repo, host the planner.

    git clone https://github.com/alladdinkumar/google-interview-prep.git my-prep
    cd my-prep
    python scripts/setup_own_copy.py --repo my-google-prep --start 2026-10-05

What it does, in order (every step is printed first; --dry-run stops there):

  1. Checks git and the GitHub CLI (gh) are installed and that gh is logged in.
  2. Clears the previous owner's personal data: ticked progress, skipped days, daily logs,
     reviews, notes, filled-in trackers, their coaching persona and archives, their LLD
     project solutions. Sets your start date and your profile for the Gemini prompts.
  3. Commits that — or, with --fresh-history, starts a new history with one commit.
  4. Creates <you>/<repo> on GitHub, pushes, turns on GitHub Pages (built by Actions),
     starts the first deploy and waits for it.
  5. Prints your planner's address and how to make the token that lets your phone tick.

Options:
  --repo NAME        name of the new GitHub repository (required unless --local-only)
  --start DATE       plan Day 1, YYYY-MM-DD; should be a Monday (default: next Monday)
  --level L4         the level you are targeting, used in the Gemini prompts (default L4)
  --hours 10         your weekly study hours, used in the Gemini prompts (default 10)
  --private          create a private repository (GitHub Pages then needs a paid plan)
  --fresh-history    start a new git history instead of keeping the original commits
  --keep-data        do not clear anything (you are moving your own copy to a new repo)
  --local-only       clear and commit locally; skip everything on GitHub
  --dry-run          print what would happen and change nothing
  --yes              do not ask for confirmation

Standard library only; works on Windows, macOS and Linux.
"""

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Files and folders that belong to whoever owned the copy before you.
PERSONAL_PATHS = ["prompt.md", "plan/archive", "docs/archive-v1", "trackers/archive-v1"]
KEEP_NAMES = {"TEMPLATE.md", "_index.md"}
STUBS_TAG = "lld-stubs"          # the commit whose projects/lld/*/src are the untouched stubs


def run(cmd, check=True, capture=True):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=capture, text=True, encoding="utf-8", errors="replace")
    if check and r.returncode != 0:
        raise SystemExit(f"\nFailed: {' '.join(cmd)}\n{(r.stderr or r.stdout).strip()}")
    return r


def say(msg=""):
    print(msg, flush=True)


def next_monday(today=None):
    today = today or dt.date.today()
    return today + dt.timedelta(days=(7 - today.weekday()) % 7 or 7)


def gh_login():
    if not shutil.which("gh"):
        return None
    r = run(["gh", "api", "user", "--jq", ".login"], check=False)
    return r.stdout.strip() if r.returncode == 0 else None


def origin_slug():
    r = run(["git", "remote", "get-url", "origin"], check=False)
    if r.returncode != 0:
        return None
    m = re.search(r"github\.com[:/](.+?)(?:\.git)?$", r.stdout.strip())
    return m.group(1) if m else None


# ---------------------------------------------------------------------------
# Clearing the previous owner's data
# ---------------------------------------------------------------------------

def personal_files():
    """Everything the reset will delete, for the confirmation list."""
    out = []
    for folder in ("daily-logs", "reviews", "notes"):
        for f in sorted((ROOT / folder).rglob("*.md")):
            if f.name not in KEEP_NAMES:
                out.append(f.relative_to(ROOT).as_posix())
    for p in PERSONAL_PATHS:
        if (ROOT / p).exists():
            out.append(p + ("/" if (ROOT / p).is_dir() else ""))
    return out


def reset(args, new_url, repo_name, dry):
    actions = []
    start = args.start
    schedule = {"skips": [], "start": start, "version": 1}
    profile = {
        "head": (f"I am preparing for the Google software engineer interview ({args.level}), writing C++. "
                 "Answer as a Google interviewer and coach would: precise, terse, no encouragement, no filler."),
        "situation": f"I study about {args.hours} hours a week, so I need answers I can use in a 45-minute slot.",
    }
    actions.append(f"write webapp/progress.json   (no sessions ticked)")
    actions.append(f"write webapp/schedule.json   (Day 1 = {start}, no skipped days)")
    actions.append(f"write webapp/profile.json    ({args.level}, ~{args.hours} h/week)")
    for f in personal_files():
        actions.append(f"delete {f}")
    actions.append("regenerate trackers/*.md as blank (scripts/trackers.py --blank)")
    has_tag = run(["git", "rev-parse", "-q", "--verify", f"refs/tags/{STUBS_TAG}"], check=False).returncode == 0
    if has_tag:
        actions.append(f"restore projects/lld/*/src to the unsolved stubs (tag {STUBS_TAG})")
    if new_url:
        actions.append(f"point README links at {new_url}")
    if dry:
        for a in actions:
            say(f"    {a}")
        return

    (ROOT / "webapp/progress.json").write_text('{\n  "done": {},\n  "version": 1\n}\n', encoding="utf-8", newline="\n")
    (ROOT / "webapp/schedule.json").write_text(json.dumps(schedule, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    (ROOT / "webapp/profile.json").write_text(json.dumps(profile, indent=2) + "\n", encoding="utf-8", newline="\n")
    for rel in personal_files():
        p = ROOT / rel.rstrip("/")
        shutil.rmtree(p) if p.is_dir() else p.unlink()
    for folder in ("notes", "reviews", "daily-logs"):          # drop folders left empty
        for d in sorted((ROOT / folder).rglob("*"), reverse=True):
            if d.is_dir() and not any(d.iterdir()):
                d.rmdir()
    run([sys.executable, "scripts/trackers.py", "--blank"])
    if has_tag:
        run(["git", "checkout", STUBS_TAG, "--", "projects/lld"])
    # Lines that describe the previous owner's archive and persona, now deleted.
    for rel in ("README.md", "plan/PLAN.md"):
        p = ROOT / rel
        lines = p.read_text(encoding="utf-8").splitlines()
        keep = [l for l in lines if "archive/v1-26-week" not in l and "`prompt.md`" not in l]
        p.write_text("\n".join(keep) + "\n", encoding="utf-8", newline="\n")
    if new_url:
        for rel in ("README.md", "webapp/README.md"):
            p = ROOT / rel
            text = p.read_text(encoding="utf-8")
            text = re.sub(r"https://[A-Za-z0-9-]+\.github\.io/[A-Za-z0-9._-]+/", new_url, text)
            text = text.replace("Only select repositories → google-interview-prep",
                                f"Only select repositories → {repo_name}")
            p.write_text(text, encoding="utf-8", newline="\n")


# ---------------------------------------------------------------------------
# GitHub
# ---------------------------------------------------------------------------

def enable_pages(slug):
    r = run(["gh", "api", "-X", "POST", f"repos/{slug}/pages", "-f", "build_type=workflow"], check=False)
    if r.returncode == 0:
        return True, ""
    if "409" in (r.stderr + r.stdout) or "already" in (r.stderr + r.stdout).lower():
        r = run(["gh", "api", "-X", "PUT", f"repos/{slug}/pages", "-f", "build_type=workflow"], check=False)
        return r.returncode == 0, r.stderr.strip()
    return False, (r.stderr or r.stdout).strip()


def wait_for_deploy(slug, timeout=420):
    run(["gh", "workflow", "run", "pages.yml", "-R", slug], check=False)
    deadline = time.time() + timeout
    time.sleep(8)
    while time.time() < deadline:
        r = run(["gh", "run", "list", "-R", slug, "--workflow", "pages.yml", "--limit", "1",
                 "--json", "status,conclusion,url"], check=False)
        try:
            runs = json.loads(r.stdout or "[]")
        except ValueError:
            runs = []
        if runs and runs[0]["status"] == "completed":
            return runs[0]["conclusion"], runs[0]["url"]
        say("    … building")
        time.sleep(15)
    return "timeout", f"https://github.com/{slug}/actions"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo")
    ap.add_argument("--start", default=next_monday().isoformat())
    ap.add_argument("--level", default="L4")
    ap.add_argument("--hours", type=int, default=10)
    ap.add_argument("--private", action="store_true")
    ap.add_argument("--fresh-history", action="store_true")
    ap.add_argument("--keep-data", action="store_true")
    ap.add_argument("--local-only", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--yes", action="store_true")
    args = ap.parse_args()

    say("\nGoogle prep planner — set up your own copy\n")

    # ---- 1. checks ------------------------------------------------------
    if not shutil.which("git"):
        raise SystemExit("git is not installed: https://git-scm.com/downloads")
    if run(["git", "rev-parse", "--show-toplevel"], check=False).returncode != 0:
        raise SystemExit("Run this from inside the cloned repository.")
    try:
        start = dt.date.fromisoformat(args.start)
    except ValueError:
        raise SystemExit(f"--start must be YYYY-MM-DD, got {args.start!r}")
    if start.weekday() != 0:
        mon = start + dt.timedelta(days=(7 - start.weekday()) % 7)
        say(f"  Note: {start} is a {start:%A}. Every plan week starts on Monday, so Saturday's four-hour")
        say(f"  block would land on a {(start + dt.timedelta(days=5)):%A}. Consider --start {mon}.\n")
    if run(["git", "status", "--porcelain"]).stdout.strip() and not args.dry_run:
        raise SystemExit("You have uncommitted changes. Commit or stash them first, so nothing is lost.")

    login = slug = new_url = None
    if not args.local_only:
        if not args.repo or not re.fullmatch(r"[A-Za-z0-9._-]+", args.repo):
            raise SystemExit("--repo NAME is required (letters, digits, . _ -), e.g. --repo my-google-prep")
        if not shutil.which("gh"):
            raise SystemExit("The GitHub CLI is needed: https://cli.github.com, then `gh auth login`.\n"
                             "Or run with --local-only and push by hand (see README → Host your own copy).")
        login = gh_login()
        if not login:
            raise SystemExit("gh is not logged in. Run `gh auth login` and try again.")
        slug = f"{login}/{args.repo}"
        new_url = f"https://{login.lower()}.github.io/{args.repo}/"
        if origin_slug() and origin_slug().lower() == slug.lower():
            raise SystemExit(f"{slug} is already this repository's origin. Pick a new --repo name.")
        if run(["gh", "repo", "view", slug], check=False).returncode == 0:
            raise SystemExit(f"{slug} already exists on GitHub. Pick another --repo name or delete it first.")
    # Refuse to wipe the data of the account that owns this copy — with or without GitHub.
    owner = login or gh_login()
    if owner and origin_slug() and origin_slug().split("/")[0].lower() == owner.lower() and not args.keep_data:
        raise SystemExit(f"This copy belongs to your own account ({origin_slug()}): clearing it would delete your\n"
                         "progress. Use --keep-data to move it to a new repo with your data.")

    # ---- plan -----------------------------------------------------------
    say(f"  GitHub account : {login or '(skipped: --local-only)'}")
    if slug:
        say(f"  New repository : {slug} ({'private' if args.private else 'public'})")
        say(f"  Planner URL    : {new_url}")
    say(f"  Plan Day 1     : {args.start}")
    say(f"  History        : {'new, one commit' if args.fresh_history else 'kept'}")
    say("\n  Changes to this folder:")
    if args.keep_data:
        say("    none (--keep-data)")
    else:
        reset(args, new_url, args.repo, dry=True)
    if args.private and slug:
        say("\n  Warning: GitHub Pages on a private repository needs GitHub Pro/Team. On a free")
        say("  account the site will not publish; the planner still works locally.")
    if args.dry_run:
        say("\nDry run: nothing was changed.")
        return
    if not args.yes:
        answer = input(f"\nType {'the repo name (' + args.repo + ')' if slug else 'yes'} to go ahead: ").strip()
        if answer != (args.repo if slug else "yes"):
            raise SystemExit("Stopped. Nothing was changed.")

    # ---- 2. clear -------------------------------------------------------
    if not args.keep_data:
        say("\nClearing the previous owner's data…")
        reset(args, new_url, args.repo, dry=False)

    # ---- 3. commit ------------------------------------------------------
    run(["git", "add", "-A"])
    if args.fresh_history:
        run(["git", "checkout", "--orphan", "setup-fresh"])
        run(["git", "add", "-A"])
        run(["git", "commit", "-m", "Start my own copy of the Google prep planner"])
        run(["git", "branch", "-D", "main"], check=False)
        run(["git", "branch", "-m", "main"])
    elif run(["git", "status", "--porcelain"]).stdout.strip():
        run(["git", "commit", "-m", "Set up my own copy: clear the previous owner's data, set my start date"])
    say("  committed")
    if args.local_only:
        say("\nDone locally. Push it to a repository of your own when ready (README → Host your own copy).")
        return

    # ---- 4. GitHub ------------------------------------------------------
    if origin_slug():
        run(["git", "remote", "rename", "origin", "upstream"], check=False)
        say(f"  the original repository is now the 'upstream' remote")
    say(f"\nCreating {slug} and pushing…")
    run(["gh", "repo", "create", slug, "--private" if args.private else "--public",
         "--description", "My Google interview prep: 72-week plan and day-by-day planner",
         "--source", ".", "--remote", "origin", "--push"])
    ok, err = enable_pages(slug)
    if not ok:
        say(f"  Could not turn on GitHub Pages automatically: {err}")
        say(f"  Do it by hand: https://github.com/{slug}/settings/pages → Source: GitHub Actions")
    else:
        say("  GitHub Pages turned on (source: GitHub Actions)")
        say("Building the site (tests run first; about a minute)…")
        result, url = wait_for_deploy(slug)
        say(f"  deploy: {result} — {url}")

    # ---- 5. next steps --------------------------------------------------
    say(f"""
Your planner: {new_url}
  (the first load after a deploy can take a minute to appear)

To tick sessions from your phone, give that browser a token — once per device:
  1. https://github.com/settings/personal-access-tokens/new
  2. Repository access: Only select repositories → {args.repo}
  3. Permissions → Repository → Contents: Read and write. Nothing else.
  4. Open the planner → Add token → paste.
  Do not use `gh auth token` there: it can write to every repository you own.

At your desk:  python webapp/server.py   (http://127.0.0.1:8766, syncs with GitHub)
""")


if __name__ == "__main__":
    main()
