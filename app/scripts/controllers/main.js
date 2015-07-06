'use strict';

/**
 * @ngdoc function
 * @name quickNewsApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the quickNewsApp
 */
angular.module('quickNewsApp')
  .controller('MainCtrl', function ($scope, $http) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    var url = 'http://localhost:5000/bbc?url=business';
    $http.get(url)
	.success(function(data, status, headers, config) {
		console.log(data);
		$scope.item = data;
		console.log($scope.item.items[0][2][0])
		// $scope.rssResponseData[postIndex].postSummary = data;
	})
	.error(function(data, status, headers, config) {
		console.log('Error loading feed: ' + postUrl + ', status: ' + status);
	});
  });
