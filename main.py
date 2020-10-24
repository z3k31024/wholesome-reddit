#! /usr/bin/env python3

import json
import requests

subr = input('Enter the subreddit:')
url = 'https://reddit.com/r/{}.json'.format(subr)
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
r = requests.get(url, headers=headers)
for post in r.json()['data']['children']:
    print('')
    print(post['data']['title'])
