'use strict';

/**
 * @ngdoc function
 * @name quickNewsApp.controller:CbcCtrl
 * @description
 * # CbcCtrl
 * Controller of the quickNewsApp
 */
angular.module('quickNewsApp')
	.controller('CbcCtrl', function($scope) {
		$scope.awesomeThings = [
			'HTML5 Boilerplate',
			'AngularJS',
			'Karma'
		];
	});