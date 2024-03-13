-- List all records with a name

SELECT score, name
    FROM second_table
    WHERE name IS NOT none
    ORDER BY score DESC;
