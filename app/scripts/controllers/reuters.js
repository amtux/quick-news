'use strict';

/**
 * @ngdoc function
 * @name quickNewsApp.controller:ReutersCtrl
 * @description
 * # ReutersCtrl
 * Controller of the quickNewsApp
 */
angular.module('quickNewsApp')
  .controller('ReutersCtrl', function ($scope, $http) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    $scope.isSet = function(checkTab) {
		return this.tab === checkTab;
	};

	$scope.setTab = function(activeTab) {
		this.tab = activeTab;
		$scope.getFeed(activeTab);
	};

	$scope.getActiveTab = function() {
		return this.tab;
	};

	$scope.getFeed = function(category) {
		/*jshint unused: false */
		$scope.loading = true;
		var url = '//quicknews.amanuppal.ca:5000/reuters?url=' + category;
		$http.get(url)
		.success(function(data, status, headers, config) {
			$scope.entries = data.items;
			console.log($scope.entries);
			$scope.loading = false;
		})
		.error(function(data, status, headers, config) {
			console.log('Error loading feed: ' + url + ', status: ' + status);
		});
	};
  });
