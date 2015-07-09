'use strict';

/**
 * @ngdoc directive
 * @name quickNewsApp.directive:errSrc
 * @description
 * # errSrc
 */
angular.module('quickNewsApp')
  .directive('errSrc', function () {
    return {
      restrict: 'A',
      link: function postLink(scope, element, attrs) {
      	element.bind('error', function() {
            if (attrs.src !== attrs.errSrc) {
              attrs.$set('src', attrs.errSrc);
            }
        });
      }
    };
  });
