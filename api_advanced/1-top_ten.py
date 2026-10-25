#!/usr/bin/python3
"""Function that queries the Reddit API and prints top 10 hot post titles."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.

    If not a valid subreddit, prints None.
    Redirects are not followed so that invalid subreddits are caught.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:alu.api.advanced:v1.0.0 (by /u/enzoasaph)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        children = response.json().get("data").get("children")
        for child in children[:10]:
            print(child.get("data").get("title"))
    except Exception:
        print(None)
