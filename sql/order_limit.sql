SELECT city, LENGTH(city) AS city_length
FROM station
ORDER BY LENGTH(city) ASC , city ASC
LIMIT 1;

SELECT city, LENGTH(city) AS city_length
FROM station
ORDER BY LENGTH(city) DESC ,  city ASC
LIMIT 1;


select 
SELECT
  CASE
    WHEN age < 18 THEN 'Minor'
    WHEN age >= 18 AND age < 65 THEN 'Adult'
    ELSE 'Senior'
  END AS age_group
FROM
from triangles ;

SELECT city, LENGTH(city) AS city_length
FROM station
ORDER BY substring(city, '\d{{4}}') DESC
LIMIT 1;