#!/usr/bin/python3
"""
Queries the Reddit API to return the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers for a
    given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid
             or a request error occurs.
    """
    # The Reddit API endpoint for subreddit info
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to comply with Reddit API guidelines
    # and prevent 'Too Many Requests' errors.
    headers = {'User-Agent': 'Custom-Python-Subscriber-Scraper/1.0'}

    try:
        # Make the GET request. Crucially, allow_redirects=False prevents
        # following redirects, which happens for invalid subreddits.
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )

        # Check for a successful response (HTTP 200 OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the 'subscribers' count value from the 'data' object
            return data.get('data', {}).get('subscribers', 0)
        else:
            # If status code is not 200 (e.g., 404 Not Found, or 302 Redirect),
            # the subreddit is considered invalid or non existant, so we return 0.
            return 0

    except requests.exceptions.RequestException:
        # Handle all request errors (network failure, timeout, etc) efficiently
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



