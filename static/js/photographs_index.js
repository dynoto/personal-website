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

	$('div#reveal_modal').on('mouseenter mouseleave',function(event){
		if(event.type == 'mouseenter'){
			$('div.reveal_overlay').fadeIn(300);
			$('div.button_group').fadeIn(300);
		}else{
			$('div.reveal_overlay').stop().fadeOut(300);
			$('div.button_group').stop().fadeOut(300);
		}
	});

	$('div.reveal_overlay > div').hide();
	$('a.overlay_trigger').click(function(){
		$('div.reveal_overlay > div').slideToggle(200);
	});
});

function BodyCtrl($scope,$http){

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
			url:'/api/photographs',
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
			$scope.images = _.union($scope.images , data.objects);
		});
	};

	$scope.updateReveal = function(idx){
		$scope.revealData = $scope.images[idx];
		$scope.revealData.index = idx;
		animateLike($scope.revealData.liked);
	};

	$scope.like = function(){
		animateLike($scope.revealData.liked);
		$http({
			method:'PUT',
			url: '/api/image/' + $scope.revealData.id + '/',
			data:{'likes':'1'},	
		}).success(function(data){
			if(!$scope.revealData.liked){
				$scope.revealData.likes += 1;
				$scope.revealData.liked = 'liked';
			}
		}).error(function(data){
			console.log(data);
		});
	};

	$scope.nextImage = function(){
		fadeImage();
		var idx = $scope.revealData.index + 1;
		if(_.isObject($scope.images[idx])){
			$scope.revealData = $scope.images[idx];
			$scope.revealData.index = idx;
		}else{
			$scope.revealData = _.first($scope.images);
			$scope.revealData.index = 0;
		}
		animateLike($scope.revealData.liked);
	};

	$scope.previousImage = function(){
		fadeImage();
		var idx = $scope.revealData.index - 1;
		if(_.isObject($scope.images[idx])){
			$scope.revealData = $scope.images[idx];
			$scope.revealData.index = idx;	
			console.log($scope.revealData);
			console.log('have previous');
		}else{
			$scope.revealData = _.last($scope.images);
			$scope.revealData.index = $scope.images.length - 1;
			console.log($scope.revealData);
			console.log('no previous');
		}
		animateLike($scope.revealData.liked);
	}
}
function fadeImage(){
	$('img.reveal_image').css({opacity:0});
	$('img.reveal_image').load(function(){
		$('img.reveal_image').stop().animate({opacity:1},500);
	});
}

function animateLike(liked){
	if(liked === 'liked'){
		$('a.like_image').addClass('liked',300);
	}else{
		$('a.like_image').removeClass('liked',300);
	}
}