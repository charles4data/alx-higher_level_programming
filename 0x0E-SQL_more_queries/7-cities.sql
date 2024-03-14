-- creates a database and cities table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates table cities with id, states_id, and name columns
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id)
);
