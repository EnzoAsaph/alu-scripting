#!/usr/bin/python3
"""Module that recursively queries Reddit API for all hot post titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of titles of all hot articles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/enzoasaph)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=30)
        if response.status_code != 200:
            return None
        data = response.json().get("data", {})
    except Exception:
        return None
    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))
    after = data.get("after")
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
