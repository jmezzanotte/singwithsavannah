$(function(){
	
	// onload animation
	$('#sws-logo').show().animate({'top' : '60%', 'visibility' : 'visible'}, 1000);
	$('#sws-logo-mobi').show().animate({'top' : '60%', 'visibility' : 'visible'}, 1000);
	$('#sws-cloud-mobi').show().animate({'top' : '40%', 'visibility' : 'visible'}, 1000);
	$('#about-overlay').show().animate({'top' : '50%', 'visibility' : 'visible'}, 1000);
	

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
	//   	console.log("yo");
	//   	$('#sws-logo-mobi').css('visibility', 'hidden'); 
	//   	//$('#sws-logo-mobi').show().animate({'top' : '80%', 'visibility' : 'visible'}, 1000);
	//   }else{

	//   	$('#sws-logo-mobi').show().animate({'top' : '60%', 'visibility' : 'visible'}, 1000);
	//   }
	// }, false);
	// Sticky nav bar  
	
	$('.secondary-topbanner').sticky({
		topSpacing : 0, 
		zIndex: 999
	});

});



