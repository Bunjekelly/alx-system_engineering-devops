#!/usr/bin/python3
""" a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """getting hot list"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    if after:
        url += f'?after={after}'

    response = requests.get(url, headers={"User-Agent": "myfirst"})

    if response.status_code == 200:
        data = response.json()['data']
        hot_list += [post['data']['title'] for post in data['children']]
        after = data['after']

        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
