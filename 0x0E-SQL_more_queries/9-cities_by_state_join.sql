-- Lists all cities in a database

SELECT cities.id, cities.name, states.name
    FROM hbtn_0d_usa.cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;
