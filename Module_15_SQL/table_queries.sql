/* Table Queries -> CREATE, SELECT, INSERT, UPDATE, ALTER, TRUNCATE, DELETE */
/* Common Constraints -> UNIQUE, NOT NULL, DEFAULT, CONSTRAINT CHECK (condition) */
/* Key Constraints -> PRIMARY KEY, FOREIGN KEY */


USE social_app;

CREATE TABLE user (
	id INT PRIMARY KEY, /* PRIMARY KEY Constraint automatically assigns UNIQUE and NOT NULL to the column */
    age INT NOT NULL,
    username VARCHAR(20) NOT NULL,
    email VARCHAR(50) UNIQUE,
    followers INT DEFAULT 0,
    following INT DEFAULT 0,
    CONSTRAINT age_check CHECK (age >= 14)
);

CREATE TABLE post (
	id INT PRIMARY KEY,
    content VARCHAR(5000) NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

/* Default values used for followers and following */
INSERT INTO user 
(id, age, username, email)
VALUES
(100, 23, "sonu.codes", "sonu@email.com");

/* Duplication Error if email already exists */
INSERT INTO user 
(id, age, username, email)
VALUES
(101, 45, "hanuman.codes", "sonu@email.com");

/* Constraint check error if age < 13, email not given */
INSERT INTO user 
(id, age, username)
VALUES
(102, 3, "priyanka.codes");

/* Default email value */
INSERT INTO user 
(id, age, username)
VALUES
(101, 23, "bubu_bankura");

/* Show specific columns from a table */
SELECT id, username FROM user;
/* Show all columns/rows from a table */
SELECT * FROM user;

/* DISTINCT keyword */
SELECT DISTINCT (age), (id), (username) FROM user; /*(entire group is distinct )*/
SELECT DISTINCT (age) FROM user; /*(entire group is distinct -> Here the group contains only the age column )*/





