$(document).ready(function(){
	console.log('ready!');
	$('.body_wrapper').hide();

	$('div#project_list').on('mouseenter mouseleave','div.title_wrapper',function(event){
		if(event.type == 'mouseenter'){
			$(this).find('div.grayscale').stop().fadeTo(200,0.43);

		}else{
			// var rand =  _.random(0,30) + _.random(1,100) * 0.01;
			// $(this).find('.title_overlay').stop().animate({'right': '-' + rand.toString() + '%'},200);
			$(this).find('div.grayscale').stop().fadeTo(200,0);
		}
	});

	$('div#project_list').on('click','div.title_wrapper',function(event){
		var title_overlay = $(this).find('.title_overlay');
		var body_wrapper = $(this).siblings('.body_wrapper');
		var grayscale = $(this).find('div.grayscale');

		if(_.isUndefined($(this).attr('open'))){
			title_overlay.stop().animate({'right':'0%'},200);
			body_wrapper.stop().slideDown(200);
			grayscale.addClass('opacity_dark');
			$(this).attr('open','-');

		}else{
			title_overlay.stop().animate({'right':'-35%'},200);	
			body_wrapper.stop().slideUp(200);	
			grayscale.removeClass('opacity_dark');
			$(this).removeAttr('open');
			// var rand =  _.random(0,30) + _.random(1,100) * 0.01;
			// $(this).find('.title_overlay').stop().animate({'right': '-' + rand.toString() + '%'},200);
			// $(this).find('div.grayscale').stop().fadeTo(200,0);
		}
	});
});


function BodyCtrl($scope,$http){
	$scope.updateProjectList = function(){
		$http({
			method:'GET',
			url:'/api/project',
			params:{
				order_by:'-id'
			}
		}).success(function(data){
			$scope.projectList = data.objects;
		});
		console.log('project list updated');
	};

	$scope.projectColumnCheck = function(index){
		imageList = $scope.projectList[index].images;
		if(_.isEmpty(imageList)){
			return 'ten';
		}else{
			return 'five';
		}
	};


	$scope.updateProjectList();
}