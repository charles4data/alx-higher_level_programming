-- Lists all shows

SELECT tv_shows.title, v_show_genres.genre_id
  FROM tv_shows
        INNER JOIN tv_show_genres
	ON tv_shows.id = v_show_genres.show_id
 ORDER BY tv_shows.title, v_show_genres.genre_id;
