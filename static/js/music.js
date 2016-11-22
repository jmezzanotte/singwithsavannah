(function($){
	
	// creates a private scope
	var playbtnGlyph = 'glyphicon glyphicon-play';
	var pausebtnGlyph = 'glyphicon glyphicon-pause';


	var audio = new Audio(); 
	var audioIndex = 1; 
	var isPlaying = false;
	var trackbox = $('#trackbox');
	var trackbar = $('.trackbar');
	var audioIcon = $('.audio-icon');
	var playingTrack = '';
	var audioExt = '.mp3';
	audioIcon.addClass(playbtnGlyph); 



	function switchTrack(event){
		if(isPlaying){
			alert(playingTrack);
			if(playingTrack != event.target.parentNode.id){
				isPlaying = true;
				// playing track will be the id of the dive 
				console.log('here');
				$('#playingTrack').addClass(playbtnGlyph); 
				$(event.target).removeClass(playbtnGlyph).addClass(pausebtnGlyph); 
				audio.src = '/static/audio/' + event.target.parentNode.id+audioExt; 
				audio.play();
			}else{
				alert('pause');
				audio.pause();
				isPlaying = false; 
				$(event.target).removeClass(playbtnGlyph).addClass(pausebtnGlyph);
			}
		}else{
			// This condition switches the audio track on if nothing is playing
			
			isPlaying = true;
			// if the track is playing put the pause button up
			alert(event.target.parentNode.id);
			$(event.target).removeClass(playbtnGlyph); 
			$(event.target).addClass(pausebtnGlyph);

			if(playingTrack != event.target.parentNode.id){
				audio.src = '/static/audio/' + event.target.parentNode.id+audioExt;
			}

			audio.play();

		}
	}

	$('.audio-icon').on('click', switchTrack);
	
	audio.ontimeupdate =  function(){
		$('.progress').attr('value', this.currentTime/this.duration);
	};








})(jQuery);