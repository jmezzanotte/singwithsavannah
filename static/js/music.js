(function($){

	//var audio = $('.audio-player')[0];	
	var audioExt = '.mp3'; 
	var isPlayer = false;
	var currentSong = '';
	var currentSongObj = null;
	var currentAudioPlayer = null;
	
	$('.trackbar').on('click', function(e){
		
		'use strict'; 
		// This line will get you to the appropriate audio player
		console.log($(e.target).parent().prev()[0]);
		var audio = $(e.target).parent().prev()[0];
		currentAudioPlayer = audio;

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
			currentAudioPlayer = null;
			console.log("Current Song" + currentSong);
			console.log(currentSongObj);
		}

		currentSongObj = $(e.target);

	});

	This will prevent the event from propagating down to the child element.
	$('.trackbar p').click(function(e){
		e.stopPropagation();
	});
	
})(jQuery);