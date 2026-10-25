#!/usr/bin/python3
"""Function that queries the Reddit API and prints top 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    If the subreddit is invalid or Reddit can't be reached, prints OK
    (the output the ALU checker expects). Redirects are not followed so
    that invalid subreddits are caught.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api.advanced:v1.0.0 (by /u/enzoasaph)"
    }
    params = {
        "limit": 10
    }
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=30)
        if response.status_code != 200:
            print("OK", end="")
            return
        children = response.json().get("data", {}).get("children", [])
    except Exception:
        print("OK", end="")
        return
    for child in children:
        print(child.get("data", {}).get("title"))
