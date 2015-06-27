'use strict';

/**
 * @ngdoc function
 * @name quickNewsApp.controller:NavbarCtrl
 * @description
 * # NavbarCtrl
 * Controller of the quickNewsApp
 */
angular.module('quickNewsApp')
  .controller('NavbarCtrl', function ($scope, $location) {
    $scope.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];
    $scope.isActive = function (viewLocation) { 
        return viewLocation === $location.path();
    };
  });
