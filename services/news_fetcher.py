#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rss_sources, feedparser
import requests, io, os, json, shutil
from pprint import pprint
from pyteaser import SummarizeUrl
from shutil import copyfile
import time
import requests

bbcRssDict = rss_sources.getBbcRss()

def getNews(rssDict):
	startTime = time.time()
	directory = "./data/"

	if not os.path.exists(directory):
		os.makedirs(directory)
		print('created file: %s' % directory)

	for key, value in rssDict.items():
		fileName = directory + key + "-write.json"
		if os.path.exists(fileName):
			os.remove(fileName)
			print('deleted existing file: %s' % fileName)
		feed = feedparser.parse(value)
		feedDict = {}
		feedCounter = 0
		for post in feed.entries[:20]: #limit to 20 entries per feed
			summary = SummarizeUrl(post.link)
			imgSearch = ("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + 
				post.title)	
			imgSearchData = requests.get(imgSearch).json()
			imgBestUrl = imgSearchData['responseData']['results'][0]['url']
			feedDict[feedCounter] = [post.title, post.link, summary, imgBestUrl]
			feedCounter += 1
		with open(fileName, 'w') as fp:
			json.dump(feedDict, fp)
		print('wrote file: %s' % fileName)

	for key,value in rssDict.items():
		source = directory + key + "-write.json"
		destination = directory + key + ".json"

		if os.path.exists(source):
			copyfile(source, destination)
			print('copied file: %s' % destination)
		else:
			print ('cannot copy file: source %s not found' % source)
	print("--- %s seconds ---\n" % (time.time() - startTime))

counter = 1
while True:
	getNews(bbcRssDict)
	print("Iteration # %d complete.\nSleeping for 10 minutes\n" % counter)
	time.sleep(600)
	counter += 1
	