-- Create table users
-- with id, email, name, country
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL,
    name varchar(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US',
    PRIMARY KEY(id),
    UNIQUE(email)
)
