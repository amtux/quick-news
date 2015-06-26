'use strict';

/**
 * @ngdoc function
 * @name quickNewsApp.controller:FeedCtrl
 * @description
 * # FeedCtrl
 * Controller of the quickNewsApp
 */
angular.module('quickNewsApp')
  .controller('FeedCtrl', function ($scope) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
  });
