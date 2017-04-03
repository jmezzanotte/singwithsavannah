$(function(){
	
	// onload animation
	$('#sws-logo').show().animate({'top' : '70%', 'visibility' : 'visible'}, 1000);
	$('#sws-logo-mobi').show().animate({'top' : '60%', 'visibility' : 'visible'}, 1000);
	$('#sws-cloud-mobi').show().animate({'top' : '40%', 'visibility' : 'visible'}, 1000);
	$('#about-overlay').show().animate({'top' : '50%', 'visibility' : 'visible'}, 1000);
	


	// Sticky nav bar 
	$('.secondary-topbanner').sticky({
		topSpacing : 0, 
		zIndex: 999
	});

});



