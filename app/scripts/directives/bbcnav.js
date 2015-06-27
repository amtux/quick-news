'use strict';

/**
 * @ngdoc directive
 * @name quickNewsApp.directive:bbcNav
 * @description
 * # bbcNav
 */
angular.module('quickNewsApp')
	.directive('bbcNav', function() {
		return {
			templateUrl: '../../views/bbcnav.html',
			restrict: 'E',
			controller: function($scope) {
				// $scope.tab = 0;

				$scope.isSet = function(checkTab) {
					return this.tab === checkTab;
				};

				$scope.setTab = function(activeTab) {
					this.tab = activeTab;
					$scope.fetchRssJson(activeTab);
				};
				$scope.getActiveTab = function() {
					return this.tab;
				};

			},
			link: function postLink(scope, element, attrs) {
				// console.log(scope.getActiveTab());
				// scope.supp();

			}
		};
	});