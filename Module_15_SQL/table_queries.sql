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



/* WHERE CLAUSE -> To specify some conditions */
INSERT INTO user 
(id, age, username, followers, following)
VALUES
(102, 15, "modna_90", 10000, 45),
(103, 15, "shruti@34", 800, 5),
(104, 15, "kakababu!!!", 100, 0);

select * from user
where (followers >= 120);

select username, followers, following from user
where (followers >= 0 AND following > 0); /* modna, shruti */

select username, age  from user
where (age BETWEEN 15 and 22); /* Inclusive */

CREATE TABLE city (
	id INT PRIMARY KEY,
    city VARCHAR(5000) NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

insert into city 
(id, city, user_id)
values
(100000, "Mumbai", 100),
(100001, "Mumbai", 101),
(100002, "Delhi", 102),
(100003, "Bankura", 103),
(100004, "Kolkata", 104);


select user_id, city from city 
where city IN ("Delhi", "Kolkata", "Bankura");

select username, email from user
WHERE username LIKE '%codes%';

select username, email from user
where username NOT LIKE '%codes%';

/* ANY and ALL are used with subqueries specifically ! */

/* LIMIT Clause */
INSERT INTO user (id, age, username, email, followers, following)
VALUES 
(105, 23, 'arjun_sky', 'arjun@gmail.com', 150, 45),
(106, 25, 'neha_codes', 'neha@yahoo.com', 1200, 300),
(107, 19, 'rahul_vibe', 'rahul@outlook.com', 50, 100),
(108, 30, 'sara_dev', 'sara@gmail.com', 850, 900),
(109, 21, 'vikram_king', 'vikram@proton.me', 10, 5),
(110, 28, 'priya_art', 'priya@gmail.com', 3400, 120),
(111, 18, 'aman_99', 'aman@gmail.com', 0, 10),
(112, 22, 'zoya_star', 'zoya@yahoo.com', 600, 580),
(113, 27, 'kabir_fit', 'kabir@gmail.com', 1500, 400),
(114, 20, 'isha_vlogs', 'isha@gmail.com', 200, 250),
(115, 31, 'amit_pro', 'amit@corporate.com', 95, 15),
(116, 16, 'riya_junior', 'riya@school.com', 500, 600),
(117, 24, 'dev_ops', 'dev@linux.org', 2100, 2100),
(118, 29, 'megha_hr', 'megha@work.com', 45, 80),
(119, 26, 'rohit_sql', 'rohit@database.com', 300, 20);


select username, email from user
where age>=20 
LIMIT 10;

/* ORDER BY Clause */
select username, age, followers from user
order by followers desc; /*default is asc*/

/* Aggregate Functions and usage of IN with Sub-queries */
select max(followers) from user;
select avg(age) from user;
select count(age) from user where age >= 20;
select count(age) from user where age IN (select min(age) from user);
select sum(followers) from user;

/* GROUP BY Clause */
/*Count number of users with specific ages (age groups)*/
select age, count(id), max(followers)
from user
group by age;

select username, age from user GROUP BY age; /* ERROR !! --> Because once grouped by, aggregation function on a column is allowed only, exception being the grouped by col itself (here age)*/

/* HAVING Clause --> WHERE applies condition to table, HAVING applies condition on a GROUP*/
select age, max(followers)
from user
GROUP BY age
HAVING max(followers) >= 750 /* This condition is applied to the whole group (here age group !)*/
order by max(followers) desc;

/* UPDATE Table */
SET SQL_SAFE_UPDATES = 0;

update user
set followers = 999, following = 999
where (followers = 0) or (following = 0);

/* DELETE Table */
delete from user
where age = 28;

/* delete * from user deletes all rows !!!!! */

/* ALTER TABLE */

/* ADD COLUMN */
alter table user 
add column interests varchar(50) default "random";

/* DROP COLUMN (delete a column) */
alter table user
drop column interests;

/* RENAME COLUMN */
alter table user
change column username username VARCHAR(25) not null unique;
/* above old and new col names are same, dtype same, constraints changed, UNIQUE added ---> But they refer to the username column ! For this Specific USE CASE MODIFY is better, as shown below*/
alter table user
change COLUMN followers subscribers INT default 0;
/* above old and new col names are different, dtype and constraints kept same ---> But they refer to the username column ! */

/* MODIFY COLUMN */
alter table user
modify following int default 10000;

INSERT INTO user (id, age, username, email)
VALUES 
(120, 23, 'poopy', 'poop@poop.com'); /* following not provided -> Default will be 10000*/

/* RENAME table */
alter table user
rename to app_user;

alter table app_user
rename to user;


/* TRUNCATE TABLE removes all table data -> all or nothing */
/* delete from user where ....some_condition.... is to delete selected rows */
/* ONDELETE = CASCADE used in FK table, not TRUNCATE ! Don't confuse :) */


