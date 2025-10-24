#!/usr/bin/python3

"""
Module: reddit_subscribers
This module defines a function that queries the Reddit API and returns the number of subscribers for a given subreddit.
"""

import requests

def number_of_subscribers(subreddit):
   """
   Queries the reddit API and returns the number of subscribers for a given subreddit.
   Args:
    subreddit(str): Te subreddit name to query.
   Returns:
     int: The number of subscribers that were found for the particular subreddit, or 0 if the subreddit      is invalid.
   """
if not isinstance(subreddit, str) or not subreddit.strip():
   return 0

url = f"https://www.reddit.com/r/{subreddit}/about.json"
headers = {"User-Agent": "Python:subreddit.subscriber.counter:v1.0 (by /u/yourusername)"}

try:
   response= requests.get(url, headers=headers, allow_redirects=False)
  
   if response.status_code == 200:
       data = response.json()
       return data.get("data", {}).get("subscribers", 0)
    else:
       return 0
except requests.RequestException:
    return 0

