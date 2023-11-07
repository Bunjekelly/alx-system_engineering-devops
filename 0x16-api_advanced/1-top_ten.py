#!/usr/bin/python3
"""a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """printing top 10 posts"""
    url = 'https://www.reddit.com/r/{}/top.json?limit=10'.format(subreddit)
    response = requests.get(url, headers={"User-Agent": "myfirst"})
    if response.status_code == 200:
        posts = response.json().get("data").get("children")
        count = 0
        for post in posts:
            print(post.get("data").get("title"))
            count += 1
    else:
        print("None")
