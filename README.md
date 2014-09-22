# ferguson-urls 

This report and underlying data represent 417,972 unique URLs that were in 
13,480,000 tweets that mentioned "ferguson" between August 10th and August
27th, 2014. You can learn more about how the data was collected 
[here](http://inkdroid.org/journal/2014/08/30/a-ferguson-twitter-archive/).

The URLs themselves were extracted from the collected Twitter data, unshortened
(using [unshrtn](http://github.com/edsu/unshrtn)) and then loaded into 
[redis](http://redis.io) in order to count them.

The tweets.tsv.gz here is a tab separated file that includes the tweeted 
URL followed by the tweet URLs for any tweets that mentioned it.

The index.html file is a report of the top 100 URLs tweeted, which indicates
whether the URL appears to have been archived by the Internet Archive. It uses
the data found in urls.json, which is generated with urls.py.

## License

Code and data are licensed with [CC-BY](https://creativecommons.org/licenses/by/2.0/)


