(function($){

	
	function labelHighlight(){
		
		console.log($(this));
		$(this).prev().animate({color: '#e95e6b'}, 300);

		$(this).animate({
			// borderBottomColor : '#99ccff', 
			'border-bottom-width' : '10px'

		}, 300);
	}

	function labelNoHighlight(){
		$(this).prev().animate({color:'#333333'}, 300);
		$(this).animate({'border-bottom-width' : '1px'})

	}

	$('input[type="text"], input[type="email"], textarea').focus(labelHighlight);
	$('input[type="text"], input[type="email"], textarea').focusout(labelNoHighlight);


})(jQuery);