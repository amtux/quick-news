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
		var url = '//52.5.127.37:5000/bbc?url=' + category
		$http.get(url)
		.success(function(data, status, headers, config) {
			console.log(data);
			$scope.item = data;
			// console.log($scope.item.items[0][2][0]);
		})
		.error(function(data, status, headers, config) {
			console.log('Error loading feed: ' + postUrl + ', status: ' + status);
		});
	};
  });
