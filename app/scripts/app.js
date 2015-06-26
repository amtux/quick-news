'use strict';

/**
 * @ngdoc overview
 * @name quickNewsApp
 * @description
 * # quickNewsApp
 *
 * Main module of the application.
 */
angular
  .module('quickNewsApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .when('/bbc', {
        templateUrl: 'views/bbc.html',
        controller: 'BbcCtrl'
      })
      .when('/cbc', {
        templateUrl: 'views/cbc.html',
        controller: 'CbcCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
