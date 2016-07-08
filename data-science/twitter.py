#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twython import Twython
from collections import Counter
import codecs

TWITTER_APP_KEY = 'x3XSjHKFtibZ9r2ogHgKFGYWc'
TWITTER_APP_KEY_SECRET = '64FCXs5td6y2J4FIvTxKRmWyonBlEJZGK3mzp6gXZiV8YNM0Ri'
TWITTER_ACCESS_TOKEN = '89854746-G2UmWLm8JVgUKugaXvmkHxo77U9y932f0MNHHFdVr'
TWITTER_ACCESS_TOKEN_SECRET = 'zBImJOfckzjxso4sT03WBwjrE8PVIDAyZuJlE7YCOJH0T'

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#EstouComLula', count=5000)
tweets = search['statuses']

words = []

for tweet in tweets:
        w = tweet['text'].split(' ')
        words = words + w

count = Counter(words)
for word in count.most_common():
    print(word)