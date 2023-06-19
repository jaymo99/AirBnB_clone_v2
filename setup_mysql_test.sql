-- This script sets a weak password for the created user
-- Make sure to change the database's password validation policy to allow
-- One way is to use:
-- 	SHOW VARIABLES LIKE 'validate%';
-- This will list any validation policies set, which can be edited by:
-- 	SET GLOBAL validate_password.check_user_name = 'OFF';
-- Make sure to replace 'validate_password.check_user_name' with the appropriate policy

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
