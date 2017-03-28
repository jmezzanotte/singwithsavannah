(function($){

	String.prototype.toProperCase = function () {
    	return this.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
	};

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
		// var audio = $(e.target).parent().prev()[0];

		var audio = null;
		if($($(e.target).parent().prev()[0]).is('audio')){
			audio = $(e.target).parent().prev()[0];
		}else{
			audio = $(e.target).parent().prev().prev()[0];
		}

		$($(audio).next()[0]).text('');

		if(currentSongObj){
			currentSongObj.removeClass('active-song');
		}

		if(currentAudioPlayer){
			currentAudioPlayer.pause();
		}

		if(currentSong != e.target.id) {
			var audioURL = $(e.target).find('.hidden').text();
			audio.src = audioURL;
			var playPromise = audio.play();
			if(playPromise !== undefined){
				playPromise.then(function(){

				}).catch(function(error){
					console.log(error.message);
					console.log('show UI element to play');
					audio.play();
				});
			}
			var nowPlaying = 'Now playing: ' + e.target.id;
			nowPlaying = nowPlaying.replace(/-/gi, ' ').toProperCase();
			currentSong = e.target.id;
			$(e.target).addClass('active-song');
			$($(audio).next()[0]).text(''); 
			$($(audio).next()[0]).text(nowPlaying);

		}else{
			audio.pause();
			currentSong = '';
			currentAudioPlayer = null;
			$($(audio).next()[0]).text('');
		}
		
		currentSongObj = $(e.target);
		currentAudioPlayer = audio;
		
		

	});

	//This will prevent the event from propagating down to the child element.
	$('.trackbar p').click(function(e){
		e.stopPropagation();
	});
	
})(jQuery);