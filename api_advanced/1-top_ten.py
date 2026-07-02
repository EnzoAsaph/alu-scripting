#!/usr/bin/python3
"""Module that queries the Reddit API for top 10 hot posts."""
import json
import urllib.request


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "python:alu.api.advanced:v1.0 (by /u/alu)"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read().decode('utf-8'))
            posts = data.get("data", {}).get("children", [])
            if not posts:
                print(None)
                return
            for post in posts:
                print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
