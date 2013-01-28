var codezero = angular.module('codezero',[]);

codezero.config(function($interpolateProvider){
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');	
});