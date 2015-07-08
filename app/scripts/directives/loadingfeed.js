'use strict';

/**
 * @ngdoc directive
 * @name quickNewsApp.directive:loadingFeed
 * @description
 * # loadingFeed
 */
angular.module('quickNewsApp')
  .directive('loadingFeed', function () {
    return {
	  template: '<div class="loading"><img src="http://www.nasa.gov/multimedia/videogallery/ajax-loader.gif" width="20" height="20" />LOADING...</div>',
      restrict: 'E',
      link: function postLink(scope, element) {
	  	scope.$watch('loading', function (val) {
	  	  if (val) {
	  	  	element.show();
	  	  } else {
	  	  	element.hide();
	  	  }
          // element.text('this is the loadingFeed directive');
	    });
      }
    };
  });
