set autocommit = 0;
SET @transfer_sum = 3640.45;
SET @acc_from = 4;
SET @acc_to = 3;

START TRANSACTION;



Update `account` set `total`= (`total`+ @transfer_sum) Where `account`.`id` LIKE @acc_to;
Update `account` set `total`= (`total`- @transfer_sum) Where `account`.`id` LIKE @acc_from;
INSERT INTO transfer(`acc_from`,`acc_to`,`amount`) VALUES (@acc_from, @acc_to, @transfer_sum);

COMMIT;