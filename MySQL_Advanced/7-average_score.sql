-- create stored procedure
-- that computes and store the score
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT;
    SET avg_score = (SELECT AVG(score) FROM corrections AS average_score WHERE average_score.user_id = user_id);
    UPDATE users SET average_score = avg_score WHERE id = user_id;
END //
DELIMITER ;
