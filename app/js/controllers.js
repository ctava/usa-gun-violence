'use strict';

angular.module('myApp.controllers', [])

 .controller('MainController', ['$scope','$cookieStore','$filter','$http','$route','$location','$q','Data',function($scope,$cookieStore,$filter,$http,$route,$location,$q,Data) {
    
    $scope.version = "1.0-1"
    $scope.currentYear = "2018"

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
    


    //signup - begin
    $scope.fetchGymName = function(gymClubID) {
      console.log('fetchGymName ' + gymClubID);
      if (gymClubID.toString().length >= 5) {
        gymClubID = $scope.zeroPad(gymClubID,6)
        $scope.currentGym = new Gym();
        //console.log('fetchGymName new Gym()');
        $scope.currentGym.gymClubID = gymClubID;
        $scope.getBoyUSAGGymnastRecords(gymClubID,function() {})
        $scope.getGirlUSAGGymnastRecords(gymClubID,function() {})
      }
      if ($scope.currentGym != null && gymClubID.toString().length == 0) {
        $scope.currentGym.gymName = null;
        $scope.currentGym = null;
      }
    }

    $scope.addInBoyRegistrationCheckoutID = function() {
      console.log('addInBoyRegistrationCheckoutID');
      angular.forEach($scope.filteredboyregistrations, function(registration) { 
        registration.checkoutID = $scope.currentCheckout.checkoutID;
      });
    };

  }]);
