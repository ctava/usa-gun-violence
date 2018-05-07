'use strict';

angular.module('myApp.controllers', [])

 .controller('MainController', ['$scope','$cookieStore','$filter','$http','$route','$location','$q','Months',function($scope,$cookieStore,$filter,$http,$route,$location,$q,Months) {
    
    $scope.version = "1.0-1";
    $scope.currentYear = "2018";
    $scope.months = null;

    $scope.areCookiesEnabled = false;
    $cookieStore.put("TestCookie", "TestCookieText");
    $scope.cookieValue = $cookieStore.get("TestCookie");
    if ($scope.cookieValue) {
        $cookieStore.remove("TestCookie");
        $scope.areCookiesEnabled = true;
    }

    $scope.years = [
      { name : '2013', value: '2013' },
      { name : '2014', value: '2014' },
      { name : '2015', value: '2015' },
      { name : '2016', value: '2016' },
      { name : '2017', value: '2017' },
      { name : '2018', value: '2018' },
    ];
    
    $scope.changeYear = function() {
      console.log('changeYear ' + $scope.currentYear);
      Months.query({"year":$scope.currentYear},function(months) {
        $scope.months = months;
        $scope.filteredmonths = months;
      });

      var image = document.getElementById("glyph");
      image.setAttribute("src","./app/img/"+$scope.currentYear+".png");
    };

  }]);
