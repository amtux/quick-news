#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rss_sources, feedparser
import requests, io, os, json, shutil
# from pprint import pprint
from pyteaser import SummarizeUrl
from shutil import copyfile
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
		feedList = []
		for post in feed.entries:
			summary = SummarizeUrl(post.link)
			# summaryJson = json.dumps(summary)

			dataHolder = {}
			dataHolder['summary'] = summary
			dataHolder['title'] = post.title
			dataHolder['pstUrl'] = post.link

			feedList.append(json.dumps(dataHolder))
		feedJson = json.dumps(feedList, sort_keys=True, indent=4)
		fileObj.write(feedJson)
		print('wrote file: %s' % fileName)
		fileObj.close

	for key,value in rssDict.items():
		source = "./data/" + key + "-write.json"
		destination = "./data/" + key + ".json"

		if os.path.exists(source):
			copyfile(source, destination)
			print('copied file: %s' % destination)
		else:
			print ('cannot copy file: source %s not found' % source)

	print("--- %s seconds ---\n" % (time.time() - startTime))

while True:
	getNews(bbcRssDict)
	