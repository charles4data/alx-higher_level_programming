$(document).ready(function() {
	$.ajax({
		url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
		dataType: 'json',
		success: function(data) {
			$('#hello').text(data.hello);
		},
		error:function() {
			$('#hello').text('Error fetching Translation');
		}
	});
});
