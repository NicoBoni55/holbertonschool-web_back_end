-- create stored procedure
-- that add new correction for a student}
DELIMITER //
CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score FLOAT)
BEGIN
    INSERT INTO projects (name)
    SELECT project_name

    WHERE NOT EXISTS (SELECT * FROM projects WHERE name = project_name);
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT ID FROM projects WHERE name = project_name), score);
END //
DELIMITER ;
