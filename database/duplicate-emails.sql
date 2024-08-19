# Write your MySQL query statement below

/*SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1*/
select DISTINCT(p1.email) as Email
from Person as p1, Person as p2
where p1.email = p2.email and p1.id!= p2.id
