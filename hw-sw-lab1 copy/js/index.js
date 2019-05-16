/*
firebase setup
*/
var command;
var myFirebaseRef = new Firebase("https://gix-510.firebaseio.com/");
myFirebaseRef.on("value", getDataFromFirebase);
function getDataFromFirebase(snapshot){
	command = snapshot.val().command;
	// while(){
	//
	// }
	switch(command){
		case "start":
			// $(".in-process").show();
			// $(".before-process").fadeOut();
			// $(".in-process").fadeIn();
			// $(".before-process").hide();

			// $(".before-process").animate({background-color: #33ccff});

			startingdate = new Date();
			var myvar = setInterval(timing,1000);
		// case "complete":

	}

	console.log(command);
}
function timing(){
	endingdate = new Date();
	counting = Math.round((endingdate - startingdate)/1000);
	$(".timer").html(counting + " s");
}
/*
  Slidemenu
*/
// (function() {
// 	var $body = document.body
// 	, $menu_trigger = $body.getElementsByClassName('menu-trigger')[0];
// 	// var $start = $body.getElementsByClassName();
// 	if ( typeof $menu_trigger !== 'undefined' ) {
// 		$menu_trigger.addEventListener('click', function() {
// 			$body.className = ( $body.className == 'menu-active' )? '' : 'menu-active';
// 		});
// 	}
// }).call(this);
// var startingtime, endingtime;
var startingdate, endingdate,counting;
$(document).ready(function (){
	$(".in-process").hide();
	var $body = document.body
	, $menu_trigger = $body.getElementsByClassName('menu-trigger')[0];
	$body.className = ( $body.className == 'menu-active' )? '' : 'menu-active';

	//animation
	//slide-up
	// $(".animsition").animsition({
	//  inClass: 'fade-in-up',
	//  outClass: 'fade-out-up',
	//  inDuration: 1500,
	//  outDuration: 800,
	//  linkElement: '.animsition-link',
	//  // e.g. linkElement: 'a:not([target="_blank"]):not([href^="#"])'
	//  loading: true,
	//  loadingParentElement: 'body', //animsition wrapper element
	//  loadingClass: 'animsition-loading',
	//  loadingInner: '', // e.g '<img src="loading.svg" />'
	//  timeout: false,
	//  timeoutCountdown: 5000,
	//  onLoadEvent: true,
	//  browser: [ 'animation-duration', '-webkit-animation-duration'],
	//  // "browser" option allows you to disable the "animsition" in case the css property in the array is not supported by your browser.
	//  // The default setting is to disable the "animsition" in a browser that does not support "animation-duration".
	//  overlay : false,
	//  overlayClass : 'animsition-overlay-slide',
	//  overlayParentElement : 'body',
	//  transition: function(url){ window.location.href = url; }
 // });
});
