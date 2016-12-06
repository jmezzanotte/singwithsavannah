(function($){

	var audio = $('#audio-player')[0];
	var audioExt = '.mp3'; 
	var isPlayer = false;
	var currentSong = '';
	var currentSongObj = null;
	
	$('.trackbar').on('click', function(e){
		
		'use strict'; 

		if(currentSongObj){
			currentSongObj.removeClass('active-song');
		}

		if(currentSong != e.target.id) {
			audio.src = '/static/audio/' + e.target.id+audioExt; 
			audio.play();
			currentSong = e.target.id;
			
			console.log(currentSongObj);
			$(e.target).addClass('active-song');
			console.log("Current Song" + currentSong);
		}else{
			audio.pause();
			currentSong = '';
			console.log("Current Song" + currentSong);
			console.log(currentSongObj);
		}

		currentSongObj = $(e.target);

	});

	// This will prevent the event from propagating down to the child element.
	$('.trackbar p').click(function(e){
		e.stopPropagation();
	});
	
})(jQuery);