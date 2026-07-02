#!/usr/bin/python3
"""Module that recursively counts keywords in Reddit hot post titles."""
import json
import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context


def count_words(subreddit, word_list, after=None, word_count=None):
    """Print sorted count of keywords in all hot posts of a subreddit."""
    if word_count is None:
        word_count = {}
    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    if after:
        url += "&after={}".format(after)
    headers = {"User-Agent": "python:alu.api.advanced:v1.0 (by /u/alu)"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            if "/r/{}/".format(subreddit) not in r.geturl():
                return
            data = json.loads(r.read().decode('utf-8')).get("data", {})
    except Exception:
        return
    after = data.get("after")
    keywords = set(w.lower() for w in word_list)
    for post in data.get("children", []):
        title = post.get("data", {}).get("title", "").lower().split()
        for word in title:
            if word in keywords:
                word_count[word] = word_count.get(word, 0) + 1
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
