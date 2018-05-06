'use strict';

/* Filters */

angular.module('myApp.filters', [])
  .filter('interpolate', ['version', function(version) {
    return function(text) {
      return String(text).replace(/\%VERSION\%/mg, version);
    };
  }])
  .filter('toLocale', function () {
    return function (item) {
        //return item;
        return new Date(item*1000);
        //return d.toString();
    };
  })
  .filter('yesno', function() {
  return function(input) {
  	var trueStrings = ['yes','true','1'];
  	var falseStrings = ['no','false','0'];
  	if (angular.isString(input))
  	{
  		if (falseStrings.indexOf(input) > -1) {
  			return "N";
  		}
  		if (trueStrings.indexOf(input) > -1) {
  			return "Y";
  		}
  	}
  	if (angular.isNumber(input)) 
  	{
  		if (input===0) return 'N';
  		if (input===1) return 'Y';
  	}
  };
});
