use ecom;

insert into customers values
(7, "Mangesh", "Kolkata");

-- Indices make Faster Retrieval when that column, here --> City is ever used in any clause.
-- Remember, they are not like variables, they are just a way for DB to know that I want to identify 
-- via that column. That's why PRIMARY_KEY column is an index already existing on the Table

/*  >>>  Index (INDEX): Speeds up SELECT queries on a column. Allows duplicates.	
	>>> Unique Index (UNIQUE INDEX): Speeds up queries AND forces every value in the column to be unique. 
	>>> Fails if duplicates exist.
    >>> Primary Key: A special type of Unique Index that also prohibits NULL values.*/
    
-- Single Column Index 
-- -----> Standard Index, will succeed even if Multiple rows have city = "Kolkata"
create index city_idx on customers(city);
select * from customers where city = "Kolkata";

-- -----> UNIQUE Index, will Throw ERROR as multiple rows have city = "Kolkata"
create UNIQUE index city_idx_2 on customers(city);
select * from customers where city = "Kolkata";



-- ----- Composite Index 
insert into customers values
(8, "Mangesh", "Kolkata");

-- ---> Standard Index --> No Error if the city_name combo contains Same city and Same
-- Person on multiple Rows. 
-- 1. Create a Composite Index on city and name
CREATE INDEX city_name_idx ON customers(city, name);
-- 2. Query that utilizes this index perfectly
SELECT * FROM customers 
WHERE city = "Kolkata" AND name = "Mangesh";
-- -- Why this is fast ? The database doesn't have to look through all cities, and then look through 
-- -- all names. It looks directly at the city_name_idx, finds "Kolkata", and instantly finds "Mangesh" 
-- -- within that subset.

-- ---> UNIQUE Index --> Error if the city_name combo contains Same city and Same
-- Person on multiple Rows. 
-- 1. Create a Composite Index on city and name
CREATE UNIQUE index city_name_idx_2 ON customers(city, name);
-- 2. Query that utilizes this index perfectly
SELECT * FROM customers 
WHERE city = "Kolkata" AND name = "Mangesh";
-- -- Why this is fast ? The database doesn't have to look through all cities, and then look through 
-- -- all names. It looks directly at the city_name_idx, finds "Kolkata", and instantly finds "Mangesh" 
-- -- within that subset.

drop index city_name_idx_2 on customers;
drop index city_name_idx on customers;


/*
But creating Indices may make the Write Operations SLOW. If majority of the operations are READ, creating 
indices are fine, IF not, its best to Update the Indices or Drop the indices after READ usage or not use 
indices at all !!!!! 
*/