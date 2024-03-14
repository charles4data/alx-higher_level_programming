-- List all shows without a genre linked

SELECT tv_shows.title, tv_shows_genres.genre_id
    FROM tv_shows
    INNER JOIN tv_shows_genres
        ON tv_shows.genre_id = tv_shows_genres.genre_id
    GROUP SET (
        tv_shows.title
        tv_shows_genres.genre_id
    )