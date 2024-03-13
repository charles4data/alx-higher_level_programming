-- computes score average

SELECT SUM(scores) / COUNT(scores) AS average
    FROM second_table;
