# Write your MySQL query statement below
select Max(Salary) as SecondHighestSalary
from Employee
where salary<(select max(salary) from Employee)