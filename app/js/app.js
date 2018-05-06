'use strict';

// Declare app level module which depends on filters, and services
angular.module('myApp', ['ngCookies','myApp.filters','myApp.services','myApp.directives','myApp.controllers','myApp.animations','ngRoute','ngAnimate','ngSanitize', 'ngCsv', 'ui.bootstrap', 'wt.responsive']).
  config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  	$routeProvider.when('/', {templateUrl: '../app/data.html', controller: 'MainController'});
    $locationProvider.html5Mode(true);
    $locationProvider.hashPrefix('!');
  }]);
