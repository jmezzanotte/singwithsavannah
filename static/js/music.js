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
		//console.log($(e.target).parent().prev()[0]);
		var audio = $(e.target).parent().prev()[0];

		if(currentSongObj){
			currentSongObj.removeClass('active-song');
		}

		if(currentAudioPlayer){
			currentAudioPlayer.pause();
		}
		if(currentSong != e.target.id) {

			var audioURL = $(e.target).find('.hidden').text();
			audio.src = audioURL;
			audio.play();
			currentSong = e.target.id;
			$(e.target).addClass('active-song');

		}else{
			audio.pause();
			currentSong = '';
			currentAudioPlayer = null;
			console.log("Current Song" + currentSong);
			console.log(currentSongObj);
		}

		currentSongObj = $(e.target);
		currentAudioPlayer = audio;

	});

	//This will prevent the event from propagating down to the child element.
	$('.trackbar p').click(function(e){
		e.stopPropagation();
	});
	
})(jQuery);