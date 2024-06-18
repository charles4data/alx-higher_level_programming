$(document).ready(function() {
	$.ajax({
		url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
		dataType: 'json',
		success: function(data) {
			const movies = data.results;
			const $movieList = $('#list_movies');

			// Loop through the movies and add list items
			movies.forEach(movie => {
				$movieList.append(`<li>${movie.title}</li>`);
			});
		},
		error:function() {
			$('#list_movies').append(`<li>Error Fetching Movies</li>`);
		}
	});
});