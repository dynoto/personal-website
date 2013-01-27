$(document).ready(function(){
	$('div.top_selector > dl > dd').click(function(){
		var top_selector = $(this).attr('selector_data');
		$('p > span.'+top_selector).addClass('selector_focus',500);
		$('p > span').not('.'+top_selector).removeClass('selector_focus',500);
	});

	var timeout = setTimeout(function() {
		$('#first_selector').addClass('glow_selector',1000);
		$('#first_selector').removeClass('glow_selector',1000);
	}, 1000);

	$('#orbit_featured').orbit({
		animation:'fade',
		pauseOnHover:true,
		startClockOnMouseOut:true,
		advanceSpeed:6000,
		animationSpeed:800
	});
});
