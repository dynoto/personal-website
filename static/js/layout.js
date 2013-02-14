var codezero = angular.module('codezero',[]);

codezero.config(function($interpolateProvider){
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');	
});

codezero.directive('fadey',function(){
return {
	restrict :'A',
	link : function(scope,elm,attrs) {
		var duration = parseInt(attrs.fadey);
		$(elm).hide();
		$(elm).fadeIn(duration);
		}
	}
});

// codezero.directive('slidy',function(){
// return {
// 	restrict:'A',
// 	link: function(scope,elm,attrs) {
// 		var duration = parseInt(attrs.slidy);
// 		$(elm).hide();
// 		$(elm).slide(duration);
// 		}
// 	}
// });