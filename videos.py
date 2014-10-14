#!/usr/bin/env python

import re
import gzip
import json

def main():
    youtube = []
    vine = []
    for line in gzip.open("urls.tsv.gz"):
        cols = line.split("\t")
        r = {
            "url": cols[0],
            "tweet_count": len(cols[1:])
        }
        if re.match("^https?://www.youtube.com", cols[0]):
            youtube.append(r)
        elif re.match("^https?://vine.co", cols[0]):
            vine.append(r)

    fh = open("youtube.js", "w")
    fh.write("var youtube = ")
    fh.write(json.dumps(youtube, indent=2))
    fh.write(";")

    fh = open("vine.js", "w")
    fh.write("var vine = ")
    fh.write(json.dumps(vine, indent=2))
    fh.write(";")


if __name__ == "__main__": 
    main()

