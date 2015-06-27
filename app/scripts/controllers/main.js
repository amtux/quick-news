'use strict';

/**
 * @ngdoc function
 * @name quickNewsApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the quickNewsApp
 */
angular.module('quickNewsApp')
	.controller('MainCtrl', function($scope, $route) {
		$scope.awesomeThings = [
			'HTML5 Boilerplate',
			'AngularJS',
			'Karma'
		];
		$scope.supp = function(vari) {
			console.log(vari);
		}
	});