# Write your MySQL query statement below

SELECT name as Customers
FROM customers AS c
LEFT JOIN orders AS o
ON c.id = o.customerId
WHERE o.customerId IS NULL

/*
SELECT
c.Name AS Customers
FROM customers AS c
LEFT JOIN orders AS o
ON c.id = o.customerid
WHERE o.customerid IS NULL
*/
