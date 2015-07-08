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
      template: '<div></div>',
      restrict: 'E',
      link: function postLink(scope, element, attrs) {
      	element.bind('error', function() {
            if (attrs.src !== attrs.errSrc) {
              attrs.$set('src', attrs.errSrc);
            }
        });
        element.text('this is the errSrc directive');
      }
    };
  });
