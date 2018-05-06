'use strict';

/* Directives */

angular.module('myApp.directives', [])
  .directive('validateEmail', function() {
  var EMAIL_REGEXP = /^[_a-z0-9]+(\.[_a-z0-9]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/;
  return {
    link: function(scope, elm) {
      elm.on("keyup",function(){
            var isMatchRegex = EMAIL_REGEXP.test(elm.val());
            if( isMatchRegex&& elm.hasClass('warning') || elm.val() == ''){
              elm.removeClass('warning');
            }else if(isMatchRegex == false && !elm.hasClass('warning')){
              elm.addClass('warning');
            }
      });
    }//link
  }//return
}).directive('validateGymclubid', function() {
  return {
    link: function(scope, elm) {
      elm.on("keyup",function(){
            var isValid = elm.val() != null;
            if( isValid&& elm.hasClass('warning') || elm.val() == ''){
              elm.removeClass('warning');
            }else if(isValid == false && !elm.hasClass('warning')){
              elm.addClass('warning');
            }
      });
    }//link
  }//return
}).directive('nextOnEnter', function () {
    return {
        restrict: 'A',
        link: function ($scope, selem, attrs) {
            selem.bind('keydown', function (e) {
                var code = e.keyCode || e.which;
                if (code === 13) {
                    e.preventDefault();
                    var pageElems = document.querySelectorAll('input, select, textarea'),
                        elem = e.srcElement
                        focusNext = false,
                        len = pageElems.length;
                    for (var i = 0; i < len; i++) {
                        var pe = pageElems[i];
                        if (focusNext) {
                            if (pe.style.display !== 'none') {
                                pe.focus();
                                break;
                            }
                        } else if (pe === e.srcElement) {
                            focusNext = true;
                        }
                    }
                }
            });
        }
    }
});
