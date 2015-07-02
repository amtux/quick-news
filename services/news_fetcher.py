#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rss_sources, feedparser
import requests, io, os, json
from pprint import pprint
from pyteaser import SummarizeUrl
import time

startTime = time.time()

bbcRssDict = rss_sources.getBbcRss()

def getNews(rssDict):
	for key, value in rssDict.items():
		fileName = "./data/" + key + ".xml"
		os.remove(fileName)
		fileObj = io.open(fileName, 'w', encoding='utf8')
		feed = feedparser.parse(value)
		for post in feed.entries:
			summary = SummarizeUrl(post.link)
			fileObj.write(post.title + ": " + json.dumps(summary) + "\n")
		fileObj.close


getNews(bbcRssDict)
print("--- %s seconds ---" % (time.time() - startTime))