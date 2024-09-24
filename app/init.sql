CREATE DATABASE IF NOT EXISTS flaskdb;
ALTER USER 'root'@'localhost' IDENTIFIED WITH 'mysql_native_password' BY 'my-secret-pw';
FLUSH PRIVILEGES;