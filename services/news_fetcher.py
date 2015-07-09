#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rss_sources, feedparser
import requests, io, os, json, shutil
from pprint import pprint
from pyteaser import SummarizeUrl
from shutil import copyfile
import time
import requests

def getNews(rssDict, service, searchedImages):
	startTime = time.time()
	directory = "./data/" + service + '/'

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
		for post in feed.entries[:10]: #limit to 10 entries per feed
			imgUrl = "none"
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
					try:
						imgUrl = imgSearchData['responseData']['results'][0]['url']
						if not 'image' in requests.get(imgUrl).headers['content-type']:
							print("MISSED FIRST IMG URL = BAD CONTENT. SECOND FETCH!")
							imgUrl = imgSearchData['responseData']['results'][1]['url']
						searchedImages[post.link] = imgUrl	# add to image cache if img found
						print('image not in cache but new one fetched for %s. done!' % post.link)
					except (TypeError, IndexError, requests.exceptions.MissingSchema):
						print('DENIAL FROM GOOGLE for %s. failed!' % post.link)
						imgUrl = "200F"
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
		source = directory +  key + "-write.json"
		destination = directory + key + ".json"

		if os.path.exists(source):
			copyfile(source, destination)
			print('copied file: %s' % destination)
		else:
			print ('cannot copy file: source %s not found' % source)
	print("--- %s seconds ---\n" % (time.time() - startTime))


searchedImages = {}
counter = 1
bbcRssDict = rss_sources.getBbcRss()
cbcRssDict = rss_sources.getCbcRss()

while True:
	getNews(bbcRssDict, 'bbc', searchedImages)
	print("SERVICE BBC COMPLETE!")

	getNews(cbcRssDict, 'cbc', searchedImages)
	print("SERVICE CBC COMPLETE!")

	print("Iteration # %d complete.\nSleeping for 1 hour\n" % counter)
	time.sleep(3600)
	counter += 1
	