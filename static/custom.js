  $(function() {
	   $('#datepicker').datepicker($.extend({
	      showMonthAfterYear: false,
	      dateFormat:'dd.mm.yy',
		changeYear:true,
		   yearRange: "-100:+0"
	    },
	    $.datepicker.regional['tr']
	  ));
	});