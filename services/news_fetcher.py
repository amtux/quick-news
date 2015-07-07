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

def getNews(rssDict, service, searchedImages):
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
			imgUrl = None
			if post.link in searchedImages:
				imgUrl = searchedImages[post.link]
				print('found image in cache for %s. done!' % post.link)
			else:
				query = post.title.split()
				query = '+'.join(query)
				imgSearch = ("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + 
					service + "+" + query)
				imgSearchRequest = requests.get(imgSearch)

				if (imgSearchRequest.status_code == 200):
					imgSearchData = imgSearchRequest.json()
					imgUrl = imgSearchData['responseData']['results'][0]['url'] #on success get best img
					searchedImages[post.link] = imgUrl	# add to image cache if img found
					print('image not in cache but new one fetched for %s. done!' % post.link)
				else:
					imgUrl = "404"
					print('image not in cache. also couldnt fetch new one for %s. failed!' % post.link)

	
			summary = SummarizeUrl(post.link)
			feedDict[feedCounter] = [post.title, post.link, summary, imgUrl]
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

searchedImages = {}
counter = 1
while True:
	getNews(bbcRssDict, 'bbc', searchedImages)
	print("Iteration # %d complete.\nSleeping for 10 minutes\n" % counter)
	time.sleep(600)
	counter += 1
	