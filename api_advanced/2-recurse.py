#!/usr/bin/python3
"""Module that recursively queries Reddit API for all hot post titles."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return list of titles of all hot articles for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:alu.api.advanced:v1.0 (by /u/alu_student)"
    }
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data", {})
    posts = data.get("children", [])
    after = data.get("after")
    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
