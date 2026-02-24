create database if not exists assignment;
use assignment;

create table employee (
	emp_id int PRIMARY key,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    dept VARCHAR(50),
    salary int not null,
    hire_date date not null
);

insert into employee 
(emp_id, first_name, last_name, dept, salary, hire_date)
values
(101, "Alice", "Johnson", "IT", 6500, "2020-03-15");

INSERT INTO employee 
(emp_id, first_name, last_name, dept, salary, hire_date)
VALUES
(102, 'Mark', 'Rivera', 'HR', 4800, '2019-07-22'),
(103, 'Sophia', 'Lee', 'Finance', 7200, '2021-01-10'),
(104, 'Daniel', 'Kim', 'IT', 5800, '2018-11-05'),
(105, 'Emma', 'Brown', 'Marketing', 5300, '2022-04-18'),
(106, 'Liam', 'Patel', 'Finance', 6900, '2020-09-29'),
(107, 'Olivia', 'Garcia', 'HR', 4600, '2017-06-30'),
(108, 'Noah', 'Thompson', 'IT', 7500, '2023-02-12'),
(109, 'Ava', 'Martinez', 'Marketing', 5100, '2019-12-02'),
(110, 'Ethan', 'Davis', 'Finance', 8000, '2016-05-14');


select * from employee;

select first_name, last_name, salary from employee;

select * from employee where dept = "IT";

select * from employee where (salary > 6000);

select * from employee
ORDER BY hire_date desc;

select DISTINCT dept from employee;

select * from employee where first_name like "a%";

select * from employee where salary between 4000 and 7000;

select avg(salary) from employee;

select dept, count(emp_id) from employee
group by dept
having count(emp_id) > 3;



