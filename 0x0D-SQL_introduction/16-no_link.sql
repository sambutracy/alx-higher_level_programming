-- List all records of the table second_table with non-null name values, displaying score and name, ordered by descending score
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;
