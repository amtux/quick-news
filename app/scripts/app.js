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
        controller: 'MainCtrl',
        controllerAs: 'main'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl',
        controllerAs: 'about'
      })
      .when('/bbc', {
        templateUrl: 'views/bbc.html',
        controller: 'BbcCtrl',
        controllerAs: 'bbc'
      })
      .when('/bbc', {
        templateUrl: 'views/bbc.html',
        controller: 'BbcCtrl',
        controllerAs: 'bbc'
      })
      .when('/cbc', {
        templateUrl: 'views/cbc.html',
        controller: 'CbcCtrl',
        controllerAs: 'cbc'
      })
      .when('/reuters', {
        templateUrl: 'views/reuters.html',
        controller: 'ReutersCtrl',
        controllerAs: 'reuters'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
