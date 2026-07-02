#!/usr/bin/python3
"""Module that queries the Reddit API for subscriber count."""
import json
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context


def number_of_subscribers(subreddit):
    """Return number of subscribers for a subreddit, or 0 if invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:alu.api.advanced:v1.0 (by /u/alu)"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            if "/r/{}/".format(subreddit) not in r.geturl():
                return 0
            data = json.loads(r.read().decode('utf-8'))
            return data.get("data", {}).get("subscribers", 0)
    except Exception:
        return 0
