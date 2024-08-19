# Write your MySQL query statement below
SELECT firstName, lastName, city, state
FROM Person AS pe LEFT JOIN Address AS ad
ON pe.personId = ad.personId

