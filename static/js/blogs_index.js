function BodyCtrl($scope,$http){

	$scope.updateBlog = function(){
		$http({
			method:'GET',
			url:'/api/article',
			params:{
				order_by:'-created'
			}
		}).success(function(data){
			$scope.articles = data.objects;
			console.log($scope.articles);
		});
	}

	$scope.updateBlog();
}