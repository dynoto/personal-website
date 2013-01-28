$(document).ready(function(){

	// BIND EVENT ON MASTER (UL) AND ITS CHILDREN (LI)
	// PREVENT UNBINDED NEW ELEMENT REPEATED BY ANGULAR
	$('ul#overlay_master').on('mouseenter mouseleave','li',function(event){
		if(event.type == 'mouseenter'){
			$(this).find('div.overlay').stop().fadeOut(300);
		}else{
			$(this).find('div.overlay').fadeIn(300);
		}
	});
});

function ImageListCtrl($scope,$http){

	$scope.orderMethod = [
		{'name':'Latest photos','value':'uploaded'},
		{'name':'Most Likes','value':'likes'},
		{'name':'Alphabetic','value':'name'}
	];

	// DEFAULT VALUE FOR SELECT OPTION, ELSE SELECT WILL SHOW BLANK (UNDESIRED)
	$scope.orderSelected = $scope.orderMethod[0].value;

	$scope.ascDesc = [
		{'name':'Ascending','value':''},
		{'name':'Descending','value':'-'}
	];

	$scope.updateImages = function(){
		$http({
			method:'GET',
			url:'/api/image/',
			params:{
				order_by:$scope.orderSelected
			}
		}).success(function(data){
			$scope.images = data.objects;
			$scope.next = data.meta.next;
			// overlayAnimation();
		});
	}

	$scope.updateImages();

	$scope.moreImages = function(){
		$http({
			method:'GET',
			url: $scope.next
		}).success(function(data){
			$scope.next = data.meta.next;
			$scope.images = $scope.images.concat(data.objects);
		});
	}

	$scope.updateReveal = function(index){
		$scope.revealData = $scope.images[index];
		console.log($scope.revealData);
	}
}

codezero.directive('fadey',function(){
return {
	restrict :'A',
	link : function(scope,elm,attrs) {
		var duration = parseInt(attrs.fadey);
		elm = jQuery(elm);
		elm.hide();
		elm.fadeIn(duration);
		}
	}
});