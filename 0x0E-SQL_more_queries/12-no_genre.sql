-- List all shows without a genre linked

SELECT tv_shows.title, tv_shows_genres.genre_id
    FROM tv_shows
    INNER JOIN tv_shows_genres
        ON tv_shows.id = tv_shows_genres.show_id
    WHERE tv_shows_genres IS NULL
    ORDER BY tv_shows.title, tv_shows_genres.genre_id;
