CREATE DATABASE college;
USE college;

/* Creating table */
create table students (
	roll_no INT,
    name VARCHAR(50),
    age INT
);

/* Inserting Rows to Tables */
insert into students values
(52, "Sourakanti", 23),
(34, "Manisha", 24);

/* Show table contents */
select * from students;