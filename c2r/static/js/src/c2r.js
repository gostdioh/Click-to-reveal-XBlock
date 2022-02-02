/* Javascript for Click2RevealXBlock. */
function C2RBlock(runtime, element, initargs) {
    /* Runtime stuff, nothing here for now */
    
    myevent();
}






    function   myevent(){
	$(".rotationA").hover(function(){
		$(".story-text").removeClass("active");
		$(".text-wrap").children().eq(0).addClass("active");
	});

	$(".rotationB").hover(function(){
		$(".story-text").removeClass("active");
		$(".text-wrap").children().eq(1).addClass("active");
	});

	$(".rotationC").hover(function(){
		$(".story-text").removeClass("active");
		$(".text-wrap").children().eq(2).addClass("active");
	});

	$(".rotationD").hover(function(){
     	$(".story-text").removeClass("active");
		$(".text-wrap").children().eq(3).addClass("active");
	});

	$(document).on('click','#goGame',function (e){
		$("html, body").animate({scrollTop:$("#games").offset().top - 100}, 500, 'swing');
	});


}




function c2r(event, showText, hideText) {
    var showFinal = '<i class="fa fa-eye" aria-hidden="true"></i> ' + showText;
    var hideFinal = '<i class="fa fa-eye" aria-hidden="true"></i> ' + hideText;
    var buttonPressed = $(event.target);
    var comment = buttonPressed.nextAll('.c2r-comment');
    
    comment.slideToggle(200, function() {
        if (comment.is(":hidden")) {
            buttonPressed.html(showFinal);
            buttonPressed.attr("aria-expanded", "false");
        } else {
            buttonPressed.html(hideFinal);
            buttonPressed.attr("aria-expanded", "true");
        }
    });
}
