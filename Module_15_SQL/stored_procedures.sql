USE ecom;

-- ==============================================================================
-- STORED PROCEDURES
-- A predefined set of SQL statements saved in the database to be executed
-- whenever needed. They are analogical to functions in programming languages.
-- ==============================================================================

-- ------------------------------------------------------------------------------
-- SCENARIO 1: Returning a Result Set (Multiple Rows)
-- When a procedure contains a SELECT statement without an INTO clause,
-- it returns a full result set, which can consist of zero, one, or multiple rows.
-- ------------------------------------------------------------------------------
DELIMITER $$

CREATE PROCEDURE get_amount_from_customer_id(IN customerID INT)
BEGIN
    -- This query selects the 'amount' column.
    -- If a customer has placed multiple orders, this will return multiple rows.
    SELECT amount
    FROM orders
    WHERE customer_id = customerID;
END $$

DELIMITER ;

-- CALLing Scenario 1:
-- Even though we provide 1 input, the result might contain multiple rows.
-- The procedure behaves like a temporary table output.
CALL get_amount_from_customer_id(1);


-- ------------------------------------------------------------------------------
-- SCENARIO 2: Returning a Scalar Value (Single Variable)
-- When we use the OUT parameter with the INTO clause, we are forced to map
-- the result to a single variable.
-- NOTE: If the SELECT query returns multiple rows, this will throw an error
-- because a single variable cannot hold multiple rows.
-- ------------------------------------------------------------------------------
DELIMITER $$

CREATE PROCEDURE get_name_from_id(IN customerID INT, OUT customerName VARCHAR(5000))
BEGIN
    -- The INTO clause directs the result of the query into the OUT parameter.
    SELECT name INTO customerName
    FROM customers
    WHERE id = customerID;
END $$

DELIMITER ;

-- CALLing Scenario 2:
-- 1. We pass a user-defined session variable (@targetName) to store the result.
CALL get_name_from_id(2, @targetName);

-- 2. We select the variable to see the result.
SELECT @targetName AS CustomerName;


-- ==============================================================================
-- CLEANUP: Dropping Procedures
-- ==============================================================================
DROP PROCEDURE IF EXISTS get_amount_from_customer_id;
DROP PROCEDURE IF EXISTS get_name_from_id;