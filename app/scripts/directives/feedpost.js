'use strict';

/**
 * @ngdoc directive
 * @name quickNewsApp.directive:feedPost
 * @description
 * # feedPost
 */
angular.module('quickNewsApp')
	.directive('feedPost', function() {
		return {
			template: '<div>{{postSummary}}</div>',
			restrict: 'E',
			scope: {
				postSummary: '@'
			},
			controller: function() {
				// console.log(summarizeUrl);

			},
			link: function postLink(scope, element, attrs) {
				
			}
		};
	});