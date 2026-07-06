#!/usr/bin/python3
"""Module that queries the Reddit API for the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Print titles of the first 10 hot posts for a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "windows:alu.api.advanced.enzo:v2.0 (by /u/EnzoAsaph)"
    }
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    if not posts:
        print(None)
        return
    for post in posts:
        print(post.get("data", {}).get("title"))
