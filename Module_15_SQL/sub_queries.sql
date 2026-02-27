use ecom;

-- Using sub-queries with WHERE
select *
from orders 
where amount > (
	select avg(amount)
    from orders
);

-- Using sub-queries with SELECT
select name, (
	select count(*) from orders
	where orders.customer_id = customers.id
) as order_count
from customers;