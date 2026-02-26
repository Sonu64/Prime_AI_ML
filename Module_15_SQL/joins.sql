create database if not exists ecom;
use ecom;

create table customers (
	id int primary key,
    name varchar(100),
    city varchar(80)
);



create table orders (
	order_id int primary key,
    customer_id int,
    amount int,
    foreign key (customer_id) references customers(id)
);

insert into customers values
(1, "Alice", "Mumbai"),
(2, "Bob", "Delhi"),
(3, "Charlie", "Bangalore"),
(4, "David", "Mumbai");
insert into customers values
(5, "Piya", "Kolkata");

insert into orders
(order_id, customer_id, amount)
values
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 4, 700);


-- Inner Join --
select * from 
customers as C 
inner join orders as O
on C.id = O.customer_id;

-- Left Join --
select * from
customers as c
left join orders as o
on c.id = o.customer_id;

insert into customers
(id, name)
values
(6, "KuchKuch");

-- Right Join --
select * from
customers as c
right join orders as o
on c.id = o.customer_id;

-- Outer Join -> Left Join UNION Right Join --
select * from
customers as c
left join orders as o
on c.id = o.customer_id
UNION
select * from
customers as c
right join orders as o
on c.id = o.customer_id;


-- Cross Join --> Match every row of 1st Table with every row of 2nd table --> Lots of Rows in output !--
select *
from customers
cross join orders;


-- Self Join --
select *  
from customers as A
join customers as B
on A.id = B.id;

-- ------ Self Join is Neccessary when we need to find those employees who also have a manager_id alongwith
-- employee_id A.id == B.manager_id => Will give us those employees who are managers of a dept.
-- as well.

