'use strict';

/**
 * @ngdoc function
 * @name quickNewsApp.controller:BbcCtrl
 * @description
 * # BbcCtrl
 * Controller of the quickNewsApp
 */
angular.module('quickNewsApp')
	.controller('BbcCtrl', function($scope, $http) {
		$scope.awesomeThings = [
			'HTML5 Boilerplate',
			'AngularJS',
			'Karma'
		];

		$scope.rssResponseData = {};

		$scope.fetchRssJson = function(itemNum) {
			var url = $scope.bbcRssList[itemNum].rssUrl;
			$http.jsonp('//ajax.googleapis.com/ajax/services/feed/load?v=2.0&num=20&callback=JSON_CALLBACK&q=' + url)
				.success(function(data, status, headers, config) {
					console.log(data);
					$scope.rssResponseStatus = data.rssResponseStatus;
					$scope.rssResponseData = data.responseData.feed.entries;
					$scope.rssResponseData[0].postSummary = 0;
				})
				.error(function(data, status, headers, config) {
					console.log('Error loading feed: ' + url + ' ,status: ' + status)
				});
		};

		$scope.updatePost = function(postIndex, postUrl) {
			console.log(postUrl);

			$http.get('http://127.0.0.1:5000/data?url=' + postUrl)
				.success(function(data, status, headers, config) {
					console.log(data);
				})
				.error(function(data, status, headers, config) {
					console.log('Error loading feed: ' + postUrl + ', status: ' + status)
				});



			$scope.rssResponseData[postIndex].postSummary = 100;
			console.log($scope.rssResponseData);
		};

		$scope.bbcRssList = [{
			name: 'top-stories',
			rssUrl: 'http://feeds.bbci.co.uk/news/rss.xml'
		}, {
			name: 'world',
			rssUrl: 'http://feeds.bbci.co.uk/news/world/rss.xml'
		}, {
			name: 'uk',
			rssUrl: 'http://feeds.bbci.co.uk/news/uk/rss.xml'
		}, {
			name: 'business',
			rssUrl: 'http://feeds.bbci.co.uk/news/business/rss.xml'
		}, {
			name: 'politics',
			rssUrl: 'http://feeds.bbci.co.uk/news/politics/rss.xml'
		}, {
			name: 'health',
			rssUrl: 'http://feeds.bbci.co.uk/news/health/rss.xml'
		}, {
			name: 'education-and-family',
			rssUrl: 'http://feeds.bbci.co.uk/news/education/rss.xml'
		}, {
			name: 'science-and-environment',
			rssUrl: 'http://feeds.bbci.co.uk/news/science_and_environment/rss.xml'
		}, {
			name: 'technology',
			rssUrl: 'http://feeds.bbci.co.uk/news/technology/rss.xml'
		}, {
			name: 'entertainment-and-arts',
			rssUrl: 'http://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml'

		}];
	});