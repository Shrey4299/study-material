-- Aggregate Functions
AVG() -- Calculates the average value.
COUNT() -- Counts the number of rows.
SUM() -- Calculates the sum of values.
MIN() -- Returns the minimum value.
MAX() -- Returns the maximum value.



-- Scalar Functions
UCASE() / UPPER() -- Converts a string to uppercase.
LCASE() / LOWER() -- Converts a string to lowercase.
LEN() / LENGTH() -- Returns the length of a string.
LEFT() -- Returns the left part of a string.
RIGHT() -- Returns the right part of a string.
TRIM() -- Removes leading and trailing spaces.
CONCAT() / CONCATENATE() -- Concatenates two or more strings.


-- String Functions
SUBSTRING() / SUBSTR() -- Extracts a substring from a string.
CHARINDEX() / POSITION() -- Returns the position of a substring in a string.
REPLACE
() -- Replaces occurrences of a substring.
REVERSE() -- Reverses a string.



-- Date and Time Functions
NOW() / CURRENT_TIMESTAMP() -- Returns the current date and time.
CURDATE() / CURRENT_DATE() -- Returns the current date.
CURTIME() / CURRENT_TIME() -- Returns the current time.
DATEPART() / EXTRACT() -- Extracts parts of a date or time.
DATEDIFF()  



-- Mathematical Functions
ABS() -- Returns the absolute value.
ROUND() -- Rounds a number to a specified number of decimal places.
CEIL() / CEILING() -- Rounds a number up.
FLOOR() -- Rounds a number down.
POWER() / POW() -- Raises a number to a power.




-- Conditional Functions
CASE
    WHEN -- Performs conditional logic in SELECT statements.
    COALESCE() -- Returns the first non-null expression among its arguments.
    NULLIF() -- Returns null if the two specified expressions are equal; otherwise, the first expression is returned.
-- Conversion Functions
CAST() -- Converts a value from one data type to another.
CONVERT() -- Converts a value from one data type to another (specific to database system).
-- Window Functions (Available in some database systems)
ROW_NUMBER() -- Assigns a unique number to each row.
RANK() / DENSE_RANK() -- Assigns a rank to each row based on the values of specified columns.
LEAD() / LAG() -- Access data from subsequent or previous rows within the result set.
