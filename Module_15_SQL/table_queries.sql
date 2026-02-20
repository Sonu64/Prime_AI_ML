/* Table Queries -> CREATE, INSERT, UPDATE, ALTER, TRUNCATE, DELETE */
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





