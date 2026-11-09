#!/usr/bin/env python3
"""Fetch GitHub stats for the repos listed in _data/github_repos.yml.

Writes _data/github_stats.json, which _includes/repo-card.html and
_includes/github-summary.html render natively. Runs in GitHub Actions with the
built-in GITHUB_TOKEN, so it never depends on a third-party card service.
"""
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone

import yaml

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get(path):
    req = urllib.request.Request(API + path)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "mahanveisi8-site-stats")
    if TOKEN:
        req.add_header("Authorization", "Bearer " + TOKEN)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        print(f"  ! {path} -> HTTP {e.code}", file=sys.stderr)
        return None
    except Exception as e:  # noqa: BLE001
        print(f"  ! {path} -> {e}", file=sys.stderr)
        return None


def main():
    cfg_path = os.path.join(ROOT, "_data", "github_repos.yml")
    with open(cfg_path, encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh)

    username = cfg["username"]
    out_repos = []

    for entry in cfg["repos"]:
        full = entry["full_name"]
        print(f"- {full}")
        data = get(f"/repos/{full}")
        if not data:
            continue
        out_repos.append({
            "full_name": data["full_name"],
            "description": data.get("description") or entry.get("description"),
            "language": data.get("language") or entry.get("language"),
            "stargazers_count": data.get("stargazers_count", 0),
            "forks_count": data.get("forks_count", 0),
            "html_url": data["html_url"],
        })

    # Overall user stats across the account's own public repos.
    user = get(f"/users/{username}") or {}
    total_stars = total_forks = 0
    owned = []
    page = 1
    while page <= 10:
        batch = get(f"/users/{username}/repos?per_page=100&type=owner&page={page}")
        if not batch:
            break
        for r in batch:
            if r.get("fork"):
                continue
            owned.append(r["full_name"])
            total_stars += r.get("stargazers_count", 0)
            total_forks += r.get("forks_count", 0)
        if len(batch) < 100:
            break
        page += 1

    # Language mix across every owned repo, normalised PER REPO.
    #
    # Summing raw byte counts is misleading here: a .ipynb file stores its
    # output images as base64 inside the notebook, so a handful of notebook
    # repos drown out everything else (it produced "Jupyter Notebook 99.7%,
    # Python 0.3%"). Instead each repo contributes one unit, split by its own
    # internal language shares, so the result reflects what is actually
    # worked in rather than which file format is bulkiest on disk.
    lang_share = {}
    counted = 0
    for full in owned:
        langs = get(f"/repos/{full}/languages") or {}
        repo_total = sum(langs.values())
        if not repo_total:
            continue
        counted += 1
        for name, count in langs.items():
            lang_share[name] = lang_share.get(name, 0.0) + count / repo_total

    languages = []
    if counted:
        for name, share in sorted(lang_share.items(), key=lambda kv: kv[1], reverse=True):
            pct = round(share * 100.0 / counted, 1)
            if pct >= 1.0:                      # drop 0.0% noise
                languages.append({"name": name, "percent": pct, "repos": round(share, 2)})

    payload = {
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S +0000"),
        "user": {
            "login": username,
            "public_repos": user.get("public_repos", 0),
            "followers": user.get("followers", 0),
            "total_stars": total_stars,
            "total_forks": total_forks,
        },
        "repos": out_repos,
        "languages": languages,
        "languages_basis": counted,
    }

    if not out_repos:
        print("No repo data fetched; leaving existing stats untouched.", file=sys.stderr)
        return 1

    out_path = os.path.join(ROOT, "_data", "github_stats.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"Wrote {out_path}: {len(out_repos)} cards, {len(languages)} languages over {counted} repos, {total_stars} stars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
