'use strict';

/**
 * @ngdoc function
 * @name quickNewsApp.controller:NavCtrl
 * @description
 * # NavCtrl
 * Controller of the quickNewsApp
 */
angular.module('quickNewsApp')
  .controller('NavCtrl', function ($scope, $location) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $scope.isActive = function (viewLocation) { 
        return viewLocation === $location.path();
    };
  });
