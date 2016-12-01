(function($){




	// Try to just switch the src out 

	var audio = $('#audio-player')[0];
	var audioExt = '.mp3'; 
	var isPlayer = false;
	var currentSong = '';
	


	$('.trackbar').on('click', function(e){
		
		'use strict'; 

		if(currentSong != $(e.target).id) {
			audio.src = '/static/audio/' + e.target.id+audioExt; 
			audio.play();
			currentSong = $(e.target).id;
			$(e.target).addClass('active-song');
		}else{
			audio.pause();
			currentSong='';
			$(e.target).removeClass('active-song');
		}

	});
	
	// creates a private scope
	// var playbtnGlyph = 'glyphicon glyphicon-play';
	// var pausebtnGlyph = 'glyphicon glyphicon-pause';


	// var audio = new Audio(); 
	// var audioIndex = 1; 
	// var isPlaying = false;
	// var trackbox = $('#trackbox');
	// var trackbar = $('.trackbar');
	// var audioIcon = $('.audio-icon');
	// var playingTrack = '';
	// var audioExt = '.mp3';
	// audioIcon.addClass(playbtnGlyph); 


	// function switchTrack(event){
	// 	if(isPlaying){
		
	// 		if(playingTrack != event.target.parentNode.id){
	// 			isPlaying = true;
	// 			// playing track will be the id of the dive 
				
	// 			$('#playingTrack').addClass(playbtnGlyph); 
	// 			$(event.target).removeClass(playbtnGlyph).addClass(pausebtnGlyph); 
	// 			audio.src = '/static/audio/' + event.target.parentNode.id+audioExt; 
	// 			audio.play();
	// 		}else{
	// 			console.log('pause');
	// 			audio.pause();
	// 			isPlaying = false; 
	// 			$(event.target).removeClass(pausebtnGlyph);
	// 			$(event.target).addClass(playbtnGlyph);
	// 		}
	// 	}else{
	// 		// This condition switches the audio track on if nothing is playing
			
	// 		isPlaying = true;
			
	// 		// if the track is playing put the pause button up
	// 		console.log(event.target.parentNode.id);
	// 		$(event.target).removeClass(playbtnGlyph); 
	// 		$(event.target).addClass(pausebtnGlyph);

	// 		if(playingTrack != event.target.parentNode.id){
	// 			audio.src = '/static/audio/' + event.target.parentNode.id+audioExt;
	// 			playingTrack = event.target.parentNode.id;
	// 		}

	// 		audio.play();

	// 	}
	// }

	// $('.audio-icon').on('click', switchTrack);
	
	// audio.ontimeupdate =  function(){
	// 	$('.progress').attr('value', this.currentTime/this.duration);
	// };








})(jQuery);