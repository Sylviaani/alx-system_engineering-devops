#!/usr/bin/python3
"""a recursive function that queries and returns a list"""

import requests

def recurse(subreddit, hot_list=[], after=None):
url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    header = {"User-Agent": "Chrome"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=header, params=params)
        response.raise_for_status()

        data = response.json()

        posts = data["data"]["children"]

        if not posts:
            return None
        for post in posts:
            title = post["data"]["title"]
            hot_list.append(title)

        next_page = data["data"]["after"]
        if next_page:
            return recurse(subreddit, hot_list, after=next_page)
        else:
            return hot_list
    except requests.exceptions.RequestException:
        return None 
