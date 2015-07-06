'use strict';

/**
 * @ngdoc directive
 * @name quickNewsApp.directive:bbcNav
 * @description
 * # bbcNav
 */
angular.module('quickNewsApp')
  .directive('bbcNav', function () {
    return {
      template: '<div></div>',
      restrict: 'E',
      link: function postLink(scope, element, attrs) {
      }
    };
  });
