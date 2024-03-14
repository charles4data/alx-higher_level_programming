-- List all shows without a genre linked

SELECT tv_shows.title, g.genre_id
  FROM tv_shows
       LEFT JOIN tv_show_genres AS g
       ON tv_shows.id = tv_show_genres.show_id
       WHERE g.genre_id IS NULL
 ORDER BY tv_shows.title, tv_show_genres.genre_id;
