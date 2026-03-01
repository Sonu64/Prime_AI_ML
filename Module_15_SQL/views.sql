use ecom;

-- -- General Usage of SQL Views
create view basic_customer_data as
select id, name from customers;

select * from basic_customer_data;
select * from basic_customer_data where name IN ("Alice", "Bob");

-- -- With Multiple Tables, Safe with Explicit naming
-- Using * automatically joins all data if a new column is ever added. But this maybe a column 
-- that we don't want to reveal to someone working only on some specific columns in the inner join view.
create view inner_join_data as
select
	cust.id as customer_id,
	cust.name as customer_name,
    cust.city as city,
    ord.order_id as order_id,
    ord.amount as order_amount
from customers as cust
inner join orders as ord
on cust.id = ord.customer_id; /* No Error as the column names are different !, Would have
been an Error if customers table also used customer_id instead of only 'id' as its PK column name !*/

select * from inner_join_data;

-- Deleting Views / Dropping
drop view inner_join_data;
drop view basic_customer_data;


