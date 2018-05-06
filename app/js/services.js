'use strict';

angular.module('myApp.services', ['ngResource'])
  .factory('Months', function($resource){
    return $resource('/yearsummary')
  });