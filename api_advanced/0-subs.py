#!/usr/bin/python3
"""DOC"""
import requests


def number_of_subscribers(subreddit):
    """DOC"""
    reddit_url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)

    header = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(reddit_url,
                            headers=header
                            )

    if response.status_code == 200:
        data = response.json()['data']
        subs = data['subscribers']
        return subs
        return 0
if __name__ == '__main__':
    # Example usage:
    existing_sub = "python"
    non_existing_sub = "thissubredditdefinitelydoesnotexist2025"

    subs_existing = number_of_subscribers(existing_sub)
    print(f"Subscribers for r/{existing_sub}: {subs_existing}")

    subs_nonexisting = number_of_subscribers(non_existing_sub)
    print(f"Subscribers for r/{non_existing_sub}: {subs_nonexisting}")

    # Example of a known invalid/redirecting case (should return 0)
    invalid_sub = "askreddit/comments/17b9b18"
    subs_invalid = number_of_subscribers(invalid_sub)
    print(f"Subscribers for r/{invalid_sub}: {subs_invalid}")
