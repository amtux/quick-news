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
		fileName = "./data/" + key + "-write.json"
		if os.path.exists(fileName):
			os.remove(fileName)
		fileObj = io.open(fileName, 'wb')
		feed = feedparser.parse(value)
		feedData = []
		for post in feed.entries:
			summary = SummarizeUrl(post.link)
			summaryJson = json.dumps(summary)

			dataHolder = {}
			dataHolder['summary'] = summaryJson
			dataHolder['title'] = post.title
			dataHolder['pstUrl'] = post.link

			feedData.append(json.dumps(dataHolder))
		feedDataJson = json.dumps(feedData, sort_keys=True, indent=4)
		
		fileObj.write(feedDataJson)
		print('wrote file: %s' % fileName)
		fileObj.close


getNews(bbcRssDict)
print("--- %s seconds ---" % (time.time() - startTime))