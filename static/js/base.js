$(function(){
	
	// onload animation
	$('#sws-logo').show().animate({'top' : '70%', 'visibility' : 'visible'}, 1000);
	$('#sws-logo-mobi').show().animate({'top' : '60%', 'visibility' : 'visible'}, 1000);
	$('#sws-cloud-mobi').show().animate({'top' : '40%', 'visibility' : 'visible'}, 1000);
	$('#about-overlay').show().animate({'top' : '50%', 'visibility' : 'visible'}, 1000);
	
	// console.log(window.screen.height);
	// console.log(window.innerHeight);
	// console.log('brow')
	// console.log(window.orientation);
	// console.log(window.matchMedia("(orientation: portrait)").media);

	// Listen for orientation changes
	// window.addEventListener("orientationchange", function() {
	//   // Announce the new orientation number
	//   // alert(window.orientation);
	//   // test to see if we are in landscape. 
	//   console.log(window.matchMedia("(orientation: landscape)").matches);
	//   if (window.matchMedia("(orientation: landscape)").matches){
	//   	console.log("In correct block")
	//   	$('#sws-logo-mobi').show().animate({'top' : '10%', 'visibility' : 'visible'}, 1000);
	//   }
	// }, false);
	// Sticky nav bar 
	$('.secondary-topbanner').sticky({
		topSpacing : 0, 
		zIndex: 999
	});

});



