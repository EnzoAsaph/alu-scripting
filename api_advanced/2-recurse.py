#!/usr/bin/python3
"""Module that recursively queries Reddit API for all hot post titles."""
import json
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context


def recurse(subreddit, hot_list=[], after=None):
    """Return list of titles of all hot articles for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {"User-Agent": "python:alu.api.advanced:v1.0 (by /u/alu)"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            if "/r/{}/".format(subreddit) not in r.geturl():
                return None
            data = json.loads(r.read().decode('utf-8')).get("data", {})
    except Exception:
        return None
    after = data.get("after")
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
