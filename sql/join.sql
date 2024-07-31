-- INNER JOIN
SELECT *
FROM table1
    INNER JOIN table2 ON table1.column_name = table2.column_name;

-- LEFT JOIN (or LEFT OUTER JOIN)
SELECT *
FROM table1
    LEFT JOIN table2 ON table1.column_name = table2.column_name;

-- RIGHT JOIN (or RIGHT OUTER JOIN)
SELECT *
FROM table1
    RIGHT JOIN table2 ON table1.column_name = table2.column_name;

-- FULL JOIN (or FULL OUTER JOIN)
SELECT *
FROM table1 FULL
    JOIN table2 ON table1.column_name = table2.column_name;

-- CROSS JOIN
SELECT * FROM table1 CROSS JOIN table2;

-- SELF JOIN
SELECT *
FROM table1 t1
    INNER JOIN table1 t2 ON t1.column_name = t2.column_name;

select city.name
from city
    join country on city.countrycode = country.code
where
    country.continent = 'Africa';

-- You are given three tables: Students,
-- Friends
-- and Packages.Students contains two columns: ID
-- and Name.Friends contains two columns: ID
-- and Friend_ID (ID of the ONLY best friend).Packages contains two columns: ID
-- and Salary (
--     offered salary in $ thousands per month
-- ).

SELECT
    students.name,
FROM students
    JOIN friends ON students.id = friends.id
    JOIN packages ON students.id = packages.id;
Where students.packages.salary < friends.packages.salary


SELECT *
FROM employees
    JOIN departments ON employees.department_id = departments.department_id
    JOIN locations ON departments.location_id = locations.location_id
WHERE employees.salary > 50000;