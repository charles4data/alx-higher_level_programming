-- creates a database and cities table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    state_id INT FOREIGN KEY(states.id) NOT NULL,
    name VARCHAR(256) NOT NULL
);