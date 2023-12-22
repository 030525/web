( function($) {
  'use strict';
$(function(e) {

/*------------------------------------------------------------------
	Intro-Slider
	-------------------------------------------------------------------*/
	$('#intro .owl-carousel').owlCarousel({
    loop:true,
    margin:0,
    nav:true,
	dots:false,
	autoplay:true,
    autoplayTimeout:3000,
    responsive:{
        0:{items:1},
        600:{items:1},
        1000:{items:1}
    }
	});
	
/*------------------------------------------------------------------
	Interet-Rates
	-------------------------------------------------------------------*/
	$('#interet-rates .owl-carousel').owlCarousel({
    loop:true,
    margin:15,
    nav:true,
	dots:false,
	autoplay:true,
    autoplayTimeout:3000,
    responsive:{
        0:{items:1},
        768:{items:2},
		1000:{items:3},
        1200:{items:4}
    }
	});

/*------------------------------------------------------------------
	Services
	-------------------------------------------------------------------*/
	$('#our-services .owl-carousel').owlCarousel({
    loop:true,
    margin:15,
    nav:true,
	dots:false,
	animateOut: 'fadeOut',
	autoplay:true,
    autoplayTimeout:3000,
    responsive:{
        0:{items:1},
        768:{items:2},
        1000:{items:4}
    }
	});
	
/*------------------------------------------------------------------
	Testimonials
	-------------------------------------------------------------------*/
	$('#testimonials .owl-carousel').owlCarousel({
    loop:true,
    margin:20,
    nav:false,
	dots:true,
	center:true,
	autoplay:true,
    autoplayTimeout: 3000,
    responsive:{
        0:{items:1},
        600:{items:1},
        1000:{items:3}
    }
	});
	
/*------------------------------------------------------------------
	Testimonials-2
	-------------------------------------------------------------------*/
	$('#testimonials2 .owl-carousel').owlCarousel({
    loop:true,
    margin:20,
    nav:false,
	dots:true,
	autoplay:true,
    autoplayTimeout: 3000,
    responsive:{
        0:{items:1},
        900:{items:2},
        1000:{items:2}
    }
	});

/*------------------------------------------------------------------
	Services-Box
	-------------------------------------------------------------------*/
	$('#services .owl-carousel').owlCarousel({
    loop:true,
    margin:30,
    nav:false,
	dots:true,
	animateOut: 'fadeOut',
	autoplay:true,
    autoplayTimeout:3000,
    responsive:{
        0:{items:1},
        600:{items:2},
        1000:{items:3}
    }
	});	


/*------------------------------------------------------------------
	Loan-Amount-Slider
	-------------------------------------------------------------------*/	
	// With JQuery
	$("#loan_amount").slider();
	$("#loan_amount").on("slide", function(slideEvt) {
		$("#loan_amountSliderVal").text(slideEvt.value);
	});

/*------------------------------------------------------------------
	Loan-Amount-Slider
	-------------------------------------------------------------------*/	
	// With JQuery
	$("#loan_period").slider();
	$("#loan_period").on("slide", function(slideEvt) {
		$("#loan_periodSliderVal").text(slideEvt.value);
	});
	
	
/*------------------------------------------------------------------
	Loan-Interest-Slider
	-------------------------------------------------------------------*/	
	// With JQuery
	$("#loan_interest").slider();
	$("#loan_interest").on("slide", function(slideEvt) {
		$("#loan_interestSliderVal").text(slideEvt.value);
	});
	
	
 
 /*------------------------------------------------------------------
	Countdown
	-------------------------------------------------------------------*/
  // 2019[year] - 4[month] - 22[day]
  
  $('#countdown').countdown('2020/6/22', function(event) { 
	$(this).html(event.strftime('<span class="countdown-period">%-D <span>Day%!D</span></span> <span class="countdown-period">%H <span>Hours</span></span> <span class="countdown-period">%M <span>Minutes</span></span> <span class="countdown-period">%S <span>Seconds</span></span>'));
  });
  
		});

		

})(jQuery);