'use strict';

/**
 * @ngdoc function
 * @name quickNewsApp.controller:BbcCtrl
 * @description
 * # BbcCtrl
 * Controller of the quickNewsApp
 */
angular.module('quickNewsApp')
  .controller('BbcCtrl', function ($scope, $http) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    $scope.postLimit = 10;

    $scope.showMorePosts = function() {
    	$scope.postLimit += 5;
    };

    $scope.isSet = function(checkTab) {
		return this.tab === checkTab;
	};

	$scope.setTab = function(activeTab) {
		this.tab = activeTab;
		$scope.postLimit = 10;
		$scope.getFeed(activeTab);
	};

	$scope.getActiveTab = function() {
		return this.tab;
	};

	$scope.getFeed = function(category) {
		/*jshint unused: false */
		$scope.loading = true;
		var url = '//quicknews.amanuppal.ca:5000/bbc?url=' + category;
		$http.get(url)
		.success(function(data, status, headers, config) {
			$scope.entries = data.items;
			$scope.numEntries = Object.keys($scope.entries).length;
			$scope.loading = false;
		})
		.error(function(data, status, headers, config) {
			console.log('Error loading feed: ' + url + ', status: ' + status);
		});
	};
  });