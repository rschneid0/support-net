$(document).ready(function() {
	$(function(){
	  $(".dropdown-menu li a").click(function(){

	    $(".btn:first-child").text($(this).text());
	     $(".btn:first-child").val($(this).text());
	  });

	  $("#go").click(function(){
    
	    var text =  $(".btn:first-child").text();
	    if(text.search(/Artists/i) < 0){
	          console.log(text);
	    };
	  });
  
	});
});
