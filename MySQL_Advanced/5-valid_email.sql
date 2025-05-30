-- create a trigger
-- that reset the attribute valid_email
DELIMITER //

CREATE TRIGGER valid_
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END//

DELIMITER ;
