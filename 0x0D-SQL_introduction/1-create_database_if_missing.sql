/*creates the database hbtn_0c_0 in your MySQL server*/

CREATE DATABASE IF NOT EXISTS hbtn_0c_0;

CREATE USER IF NOT EXISTS 'highrate12'@'localhost' IDENTIFIED BY 'highrate';

GRANT ALL PRIVILEGES ON hbtn_0c_0.* TO 'highrate12'@'localhost';
