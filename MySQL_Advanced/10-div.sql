-- creates a function SafeDiv that divides
-- the first by the second number
DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;

    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END $$

DELIMITER ;
