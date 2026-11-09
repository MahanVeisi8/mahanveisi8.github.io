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
    lang_bytes = {}

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
        langs = get(f"/repos/{full}/languages") or {}
        for name, count in langs.items():
            lang_bytes[name] = lang_bytes.get(name, 0) + count

    # Overall user stats: count stars/forks across the account's public repos.
    user = get(f"/users/{username}") or {}
    total_stars = total_forks = 0
    page = 1
    while page <= 10:
        batch = get(f"/users/{username}/repos?per_page=100&type=owner&page={page}")
        if not batch:
            break
        for r in batch:
            if r.get("fork"):
                continue
            total_stars += r.get("stargazers_count", 0)
            total_forks += r.get("forks_count", 0)
        if len(batch) < 100:
            break
        page += 1

    total_bytes = sum(lang_bytes.values()) or 1
    languages = [
        {"name": n, "bytes": b, "percent": round(b * 100.0 / total_bytes, 1)}
        for n, b in sorted(lang_bytes.items(), key=lambda kv: kv[1], reverse=True)
    ]

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
    }

    if not out_repos:
        print("No repo data fetched; leaving existing stats untouched.", file=sys.stderr)
        return 1

    out_path = os.path.join(ROOT, "_data", "github_stats.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"Wrote {out_path}: {len(out_repos)} repos, {len(languages)} languages, {total_stars} stars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
