 Aggregate Functions
$avg -- Calculates the average value.
$count -- Counts the number of documents.
$sum -- Calculates the sum of values.
$min -- Returns the minimum value.
$max -- Returns the maximum value.


-- String Functions
$toUpper -- Converts a string to uppercase.
$toLower -- Converts a string to lowercase.
$strLenCP -- Returns the length of a string in code points.
$substrCP -- Extracts a substring from a string.
$concat -- Concatenates two or more strings.
$trim -- Removes leading and trailing spaces.
$replaceAll -- Replaces occurrences of a substring with another string.
$reverseArray -- Reverses the order of elements in an array.


-- Date and Time Functions
$currentDate -- Returns the current date and time.
$dateFromParts -- Creates a date from year, month, day, and other parts.
$dateAdd -- Adds a specified time period to a date.
$dateSubtract -- Subtracts a specified time period from a date.
$dayOfMonth -- Returns the day of the month from a date.
$month -- Returns the month from a date.
$year -- Returns the year from a date.


-- Mathematical Functions
$abs -- Returns the absolute value.
$round -- Rounds a number to a specified number of decimal places.
$ceil -- Rounds a number up.
$floor -- Rounds a number down.
$pow -- Raises a number to a power.
$sqrt -- Returns the square root of a number.


-- Conditional Functions
$cond -- Performs conditional logic within an aggregation pipeline.
$ifNull -- Returns the first non-null value from a list of expressions.
$switch -- Evaluates multiple expressions and returns a result based on the first matched condition.


-- Conversion Functions
$convert -- Converts a value to a specified data type.
$toString -- Converts a value to a string.
$toInt -- Converts a value to an integer.
$toDouble -- Converts a value to a double.


-- Array Functions
$arrayElemAt -- Returns the element at the specified array index.
$filter -- Filters the elements of an array based on a condition.
$map -- Applies an expression to each element of an array.
$reduce -- Reduces an array to a single value based on an accumulator function.
