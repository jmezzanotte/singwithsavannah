(function($) {
  
    // Toggle Nav on Click
    $('.toggle-nav').click(function() {
        // Calling a function in case you want to expand upon this.
        toggleNav();
        $('.hamburger').toggleClass('is-active');
        $('#home-nav-close').toggleClass('is-active');
    });

    function toggleNav() {
    if ($('#site-wrapper').hasClass('show-nav')) {
        // Do things on Nav Close
        $('#site-wrapper').removeClass('show-nav');
    } else {
        // Do things on Nav Open
        $('#site-wrapper').addClass('show-nav');
    }

    //$('#site-wrapper').toggleClass('show-nav');
}
  
})(jQuery);

