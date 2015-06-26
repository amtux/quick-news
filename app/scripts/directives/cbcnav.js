'use strict';

/**
 * @ngdoc directive
 * @name quickNewsApp.directive:cbcNav
 * @description
 * # cbcNav
 */
angular.module('quickNewsApp')
  .directive('cbcNav', function () {
    return {
      template: '<div></div>',
      restrict: 'E',
      link: function postLink(scope, element, attrs) {
        element.text('this is the cbcNav directive');
      }
    };
  });
