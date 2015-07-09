#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rss_sources, feedparser
import requests, io, os, json, shutil
from pprint import pprint
from pyteaser import SummarizeUrl
from shutil import copyfile
import time, requests, urllib2

def getNews(rssDict, service, searchedImages):
	startTime = time.time()
	directory = "./data/" + service + '/'
	# create directory for service if doesnt yet exist
	if not os.path.exists(directory):
		os.makedirs(directory)
		print('created file: %s' % directory)
	# iterate each feed in service -> fetch data -> write to temp file -> copy to actual file
	for key, value in rssDict.items():
		fileName = directory + key + "-write.json"
		# delete {category}-write.json file if one already exists
		if os.path.exists(fileName):
			os.remove(fileName)
			print('deleted existing file: %s' % fileName)
		feed = feedparser.parse(value) #parse feed to get all the posts
		feedDict = {}
		feedCounter = 0
		# loop through posts in category
		for post in feed.entries[:10]: #limit to 10 entries per feed
			imgUrl = "none"
			# caching enabled. this prevents asking google for images every-time
			if post.link in searchedImages:
				imgUrl = searchedImages[post.link]
				print('found image in cache for %s. done!' % post.link)
			else:
				query = post.title.split()
				query = '+'.join(query)
				imgSearch = ("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + 
					service + "+" + query)

				imgSearchRequest = requests.get(imgSearch)

				if (imgSearchRequest.status_code == 200): #on get success
					imgSearchData = imgSearchRequest.json()
					try:
						imgUrl = imgSearchData['responseData']['results'][0]['url']
						imgUrl = urllib2.unquote(imgUrl);
						# check if select url is actually an image
						# if not, choose the next url
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
	
			summary = SummarizeUrl(post.link) # summarize text from article
			feedDict[feedCounter] = [post.title, post.link, summary, imgUrl]
			feedCounter += 1
		# write the collected data to {category}-write.json in json format
		with open(fileName, 'w') as fp:
			json.dump(feedDict, fp)
		print('wrote file: %s' % fileName)
	# iterate through all cateogries and copy temp files to the actual files
	for key,value in rssDict.items():
		source = directory +  key + "-write.json"
		destination = directory + key + ".json"
		if os.path.exists(source):
			copyfile(source, destination)
			print('copied file: %s' % destination)
		else:
			print ('cannot copy file: source %s not found' % source)
	print("--- %s seconds ---\n" % (time.time() - startTime)) #iteration runtime


searchedImages = {} # variable for caching google image urls
counter = 1 # count the iterations of while loop
bbcRssDict = rss_sources.getBbcRss()
cbcRssDict = rss_sources.getCbcRss()
reutersRssDict = rss_sources.getReutersRss()

while True:
	getNews(bbcRssDict, 'bbc', searchedImages)
	print("SERVICE BBC COMPLETE!")

	getNews(cbcRssDict, 'cbc', searchedImages)
	print("SERVICE CBC COMPLETE!")

	getNews(reutersRssDict, 'reuters', searchedImages)
	print("SERVICE REUTERS COMPLETE!")

	print("Iteration # %d complete.\nSleeping for 1 hour\n" % counter)
	time.sleep(3600)
	counter += 1
	