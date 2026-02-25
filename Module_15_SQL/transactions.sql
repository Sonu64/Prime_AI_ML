create database if not exists bank;
use bank;

show tables;

create table accounts (
	id int primary key auto_increment,
    name varchar(100) not null,
    balance decimal(10,2)
);

insert into accounts
(name, balance)
values
('Adam', 500.00),
('Bob', 300.00),
('Charlie', 1000.00);

select @@autocommit;
set autocommit = 0;

/* TRANSACTION TO DO A SAMPLE MONEY TRANSACTION B/W 2 ACCOUNTS */
start TRANSACTION;
update accounts set balance = balance - 50 where id = 1;
update accounts set  balance = balance + 50 where id = 2;
commit;

select * from accounts;

/* A Demo transaction where both users get cashback of Rs.25/- wheather they send or receive money */
DELIMITER //

CREATE PROCEDURE SafeTransfer(IN sender_id INT, IN receiver_id INT, IN amount DECIMAL(10,2))
BEGIN
    START TRANSACTION;

    -- Step 1: Debit from Sender
    UPDATE accounts SET balance = balance - amount WHERE id = sender_id;
    
    -- If sender doesn't exist, kill the whole thing
    IF ROW_COUNT() = 0 THEN
        ROLLBACK;
    ELSE
        -- Step 2: Credit to Receiver
        UPDATE accounts SET balance = balance + amount WHERE id = receiver_id;
        
        -- If receiver doesn't exist, kill the whole thing
        IF ROW_COUNT() = 0 THEN
            ROLLBACK;
        ELSE
            -- MAIN TRANSFER SUCCESSFUL
            SAVEPOINT after_wallet_topup;
            
            -- Step 3: Cashbacks
            UPDATE accounts SET balance = balance + 25 WHERE id IN (sender_id, receiver_id);
            
            -- If we didn't get exactly 2 cashbacks, just undo the cashback part
            IF ROW_COUNT() < 2 THEN
                ROLLBACK TO after_wallet_topup;
            END IF;
            
            -- FINAL SAVE
            COMMIT;
        END IF;
    END IF;
END //

DELIMITER ;