#!/usr/bin/python3
"""Module that recursively counts keywords in Reddit hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """Print a sorted count of given keywords in all hot post titles."""
    if word_count is None:
        word_count = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu.api.advanced:v1.0 (by /u/enzoasaph)"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=30)
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
    except Exception:
        return
    keywords = set(w.lower() for w in word_list)
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in keywords:
                word_count[word] = word_count.get(word, 0) + 1
    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, word_count)
    multiplier = {}
    for w in word_list:
        wl = w.lower()
        multiplier[wl] = multiplier.get(wl, 0) + 1
    final = {}
    for word, cnt in word_count.items():
        final[word] = cnt * multiplier.get(word, 1)
    for word, cnt in sorted(final.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, cnt))
