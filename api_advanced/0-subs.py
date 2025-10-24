#!/usr/bin/python3
"""Fetches the number of subscribers for a given subreddit using Reddit API.

This module defines a single function:
    number_of_subscribers(subreddit)
which returns the number of subscribers (not active users) for a subreddit.
If the subreddit is invalid, it returns 0.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): The subreddit name.

    Returns:
        int: Number of subscribers or 0 if invalid subreddit.
    """
    if not isinstance(subreddit, str) or not subreddit.strip():
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (compatible; RedditSubscriberChecker/1.0; "
            "+https://github.com/Meghan-ke)"
        )
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data.get("data", {}).get("subscribers", 0)
        return 0

    except requests.RequestException:
        return 0


