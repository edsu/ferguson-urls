#!/usr/bin/env python

import re
import bs4
import gzip
import json
import urllib
import requests

LIMIT = 100

def archived(url):
    ia = "http://web.archive.org/cdx/search/cdx"
    params = {"output": "json", "url": url}
    try:
        results = requests.get(ia, params=params)
        return len(results.json()) > 0
    except:
        return False

def title(url):
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.122 Safari/537.36'}
        resp = requests.get(url, headers=headers)
        if 'text/html' in resp.headers['content-type']:
            html = resp.content
            soup = bs4.BeautifulSoup(html)
            return soup.title.text
        else:
            return None
    except:
        return None

def main():
    urls = []
    for line in gzip.open("urls.tsv.gz"):
        cols = line.split("\t")
        r = {
            "url": cols[0],
            "tweet_sample": cols[1:10],
            "tweet_count": len(cols[1:]),
            "archived": archived(cols[0]),
            "title": title(cols[0])
        }
        urls.append(r)
        if len(urls) > LIMIT:
            break
    open('urls.json', 'w').write(json.dumps(urls, indent=2))

if __name__ == "__main__": 
    main()

