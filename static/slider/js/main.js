

(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	var carousel = function() {
		$('.home-slider').owlCarousel({
	    loop:true,
	    autoplay: true,
	    margin:0,
	    animateOut: 'fadeOut',
	    animateIn: 'fadeIn',
	    nav:true,
	    dots: true,
	    autoplayHoverPause: false,
	    items: 1,
	    navText : ["<span class='ion-ios-arrow-back'></span>","<span class='ion-ios-arrow-forward'></span>"],
	    responsive:{
	      0:{
	        items:1
	      },
	      600:{
	        items:1
	      },
	      1000:{
	        items:1
	      }
	    }
		});

	};
	carousel();

})(jQuery);

/* ==============================================
    CUSTOM SELECT
  ============================================== */
  const sorting = document.querySelector('.selectpicker');
  const commentSorting = document.querySelector('.selectpicker');
  const sortingchoices = new Choices(sorting, {
	  placeholder: false,
	  itemSelectText: ''
  });
  
  
  // Trick to apply your custom classes to generated dropdown menu
  let sortingClass = sorting.getAttribute('class');
  window.onload= function () {
	  sorting.parentElement.setAttribute('class', sortingClass);
  }

// Dropdown Searchbar
(() => {

	const form = document.getElementById('autoform');
  
	form.addEventListener('submit', e => {
  
	  e.preventDefault();
  
	  console.clear();
	  console.log('Submit disabled. Data:');
  
	  const data = new FormData(form);
  
	  for (let nv of data.entries()) {
		console.log(`${ nv[0] }: ${ nv[1] }`);
	  }
  
	});
  
  })();

  