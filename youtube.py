#!/usr/bin/env python

import re
import gzip
import json

def main():
    urls = []
    for line in gzip.open("urls.tsv.gz"):
        cols = line.split("\t")
        if not re.match("^https?://www.youtube.com", cols[0]):
            continue
        r = {
            "url": cols[0],
            "tweet_count": len(cols[1:])
        }
        urls.append(r)
    fh = open("youtube.js", "w")
    fh.write("var youtube = ")
    fh.write(json.dumps(urls, indent=2))
    fh.write(";")

if __name__ == "__main__": 
    main()

