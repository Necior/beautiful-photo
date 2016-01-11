#!/usr/bin/env python3

import random
import feedparser


def get_random_wallpaper_url():
    feed = feedparser.parse('https://www.pexels.com/rss/')
    return random.choice(feed['entries'])['href']


if __name__ == '__main__':
    print(get_random_wallpaper_url())
