#!/usr/bin/python3
"""Function that queries the Reddit API and prints top 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    If not a valid subreddit, prints None.
    Redirects are not followed so that invalid subreddits are caught.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "mozilla/5.0"}
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
    except Exception:
        return
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        title = post.get("data", {}).get("title")
        if title:
            print(title)
