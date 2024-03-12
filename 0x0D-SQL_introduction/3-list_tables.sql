-- Capture Database name
SET @db_name = (
    SELECT SUBSTRING_INDEX(@@version_info, '-', -2)
);

-- Check if the database name is empty
IF @db_name IS NULL OR @db_name = ''
BEGIN
    RAISERROR('Please provide the database name.', 16, 1);
    RETURN;
END;

-- Switch to the provided database
USE @db_name;

-- List the tables in the database
SHOW TABLES;
