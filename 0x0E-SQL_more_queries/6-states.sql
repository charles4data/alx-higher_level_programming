-- creates a db and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates table with id and name columns
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
