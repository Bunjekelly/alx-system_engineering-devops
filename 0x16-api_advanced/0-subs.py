#!/usr/bin/python3
"""a function that queries the Reddit API and returns
the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """gets number of reddit subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "myfirst"})
    if response.status_code == 200:
        data = response.json().get("data")
        return data.get("subscribers")
    else:
        return 0
