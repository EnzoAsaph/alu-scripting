#!/usr/bin/python3
"""Function that queries the Reddit API and prints top 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): the subreddit name to query.

    If not a valid subreddit, prints None.
    Redirects are not followed so that invalid subreddits are caught.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/enzoasaph)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=30)
    except Exception:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print(None)
        return

    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
