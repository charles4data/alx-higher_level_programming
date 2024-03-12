-- Lists all records in second table

SELECT CONCAT(score | name) FROM second_table GROUP BY score ASC;
