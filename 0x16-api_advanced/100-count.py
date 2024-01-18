#!/usr/bin/python3
"""a recursive function that prints sorted count of given keywords"""

import requests

def count_words(subreddit, word_list, after=None, word_counts=None):
    user_agent = 'Sylvia Ani'
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': user_agent}
    params = {'limit': 100}

    if after:
        params['after'] = after
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code != 200:
        return None
    posts = response.json().get('data').get('children')
    word_counts = word_counts or {}
    for post in posts:
        title = post["data"]["title"]
        for word in word_list:
            if word.lower() in title.lower():
                # get the value of the key, if it doesn't exist, return 0
                word_counts[word.lower()] = word_counts.get(
                    word.lower(), 0) + 1
    after = response.json()["data"]["after"]
    if after is None:
        if not word_counts:
            return
        for key, value in sorted(word_counts.items(), key=lambda x: (-x[1],
                                                                     x[0])):
            print("{}: {}".format(key.lower(), value))
        return
    return count_words(subreddit, word_list, after, word_counts)
