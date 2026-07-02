# API Advanced

## Description

This project focuses on advanced usage of APIs using Python, specifically the Reddit API. It covers making HTTP requests, handling pagination, recursive function calls, and data parsing/sorting.

## Requirements

- Python 3 (version 3.4.3)
- `requests` module
- Custom User-Agent header required for Reddit API

## Tasks

### 0. How many subs?
`0-subs.py` — Returns the number of subscribers for a given subreddit. Returns 0 for invalid subreddits.

### 1. Top Ten
`1-top_ten.py` — Prints the titles of the first 10 hot posts for a given subreddit. Prints None for invalid subreddits.

### 2. Recurse it!
`2-recurse.py` — Recursively fetches and returns a list of titles of all hot articles for a given subreddit. Returns None for invalid subreddits.

### 3. Count it!
`3-count.py` — Recursively counts keyword occurrences in hot post titles and prints results sorted by count (descending), then alphabetically.
