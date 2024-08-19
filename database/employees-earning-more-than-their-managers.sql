# Write your MySQL query statement below
 SELECT e1.name as Employee
 FROM Employee as e1 INNER JOIN Employee as e2
 WHERE e2.id = e1.managerId
    AND e1.salary > e2.salary

