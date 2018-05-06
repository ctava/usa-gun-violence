'use strict';

angular.module('myApp.services', ['ngResource'])
  .factory('Data', function($resource){
    return $resource('/data')
  });