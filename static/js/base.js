$(function(){
	
	// onload animation
	$('#headline-wrapper').show().animate({'top' : '50%', 'visibility' : 'visible'}, 1000);


	// Sticky nav bar 
	$('.secondary-topbanner').sticky({
		topSpacing : 0, 
		zIndex: 999
	});

});



