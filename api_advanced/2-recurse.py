#!/usr/bin/python3
"""Fetch all hot posts from a subreddit using Reddit API."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Recursively fetch hot posts from a subreddit."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'linux:0:1.0 (by /u/JuiceExtension6952)'}
    params = {'after': after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    json_res = response.json()
    after = json_res.get('data', {}).get('after')
    hot_articles = json_res.get('data', {}).get('children', [])

    for article in hot_articles:
        title = article.get('data', {}).get('title')
        if title:
            hot_list.append(title)

    # If there's a next page, continue recursion
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list

