-- Lists all cities in a database

SELECT cities.id, cities.name, states.name
    FROM hbtn_0d_usa.cities
    LEFT OUTER JOIN states ON states.id
    ORDER BY cities.id ASC;
