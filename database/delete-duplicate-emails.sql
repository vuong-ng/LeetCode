# Write your MySQL query statement below
/*
DELETE p2
FROM Person AS p1 JOIN 
(
  SELECT *
  FROM Person
  GROUP BY email
  HAVING COUNT(email) > 2
) AS 
*/
DELETE p1
FROM Person p1 JOIN Person p2
where p1.email = p2.email and p1.id > p2.id

