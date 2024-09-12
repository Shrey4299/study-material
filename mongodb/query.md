Comparison Operators


$eq -- Matches values that are equal to a specified value.
$ne -- Matches values that are not equal to a specified value.
$gt -- Matches values that are greater than a specified value.
$gte -- Matches values that are greater than or equal to a specified value.
$lt -- Matches values that are less than a specified value.
$lte -- Matches values that are less than or equal to a specified value.
$in -- Matches any of the values specified in an array.
$nin -- Matches none of the values specified in an array.
Logical Operators


$and -- Joins query clauses with a logical AND.
$or -- Joins query clauses with a logical OR.
$not -- Inverts the effect of a query expression.
$nor -- Joins query clauses with a logical NOR (NOT OR).
Element Operators


$exists -- Matches documents that have the specified field.
$type -- Matches documents where the field is of the specified type.
Evaluation Operators


$expr -- Allows the use of aggregation expressions within the query language.
$jsonSchema -- Matches documents that satisfy the specified JSON schema.
Array Operators


$all -- Matches arrays that contain all elements specified in the query.
$elemMatch -- Matches documents that contain an array field with at least one element that matches all the specified query criteria.
$size -- Matches any array with the specified number of elements.
Update Operators


$set -- Sets the value of a field in a document.
$unset -- Removes the specified field from a document.
$inc -- Increments the value of a field by a specified amount.
$mul -- Multiplies the value of a field by a specified amount.
$rename -- Renames a field in a document.
$min -- Updates the field only if the specified value is less than the current field value.
$max -- Updates the field only if the specified value is greater than the current field value.
$currentDate -- Sets the value of a field to the current date or timestamp.
$addToSet -- Adds a value to an array only if the value does not already exist in the array.
$pop -- Removes the first or last item of an array.
$pull -- Removes all instances of a value from an array.
$push -- Adds an item to an array.
Element Matching Operators


$regex -- Matches documents where the value of a field matches a specified regular expression.
$text -- Performs text search on the content of fields indexed with a text index.
$where -- Matches documents based on JavaScript expressions.
Geospatial Operators


$geoWithin -- Matches documents where the field value is within a specified geometry.
$geoIntersects -- Matches documents where the field value intersects with a specified geometry.
$near -- Matches documents within a specified distance from a point.
$nearSphere -- Matches documents within a specified distance from a point on a sphere.
Aggregation Pipeline Operators


$addFields -- Adds new fields to documents.
$bucket -- Categorizes documents into buckets based on a specified range.
$bucketAuto -- Automatically categorizes documents into buckets based on a specified range.
$collStats -- Returns statistics about a collection.
$count -- Counts the number of documents that pass a certain condition.
$facet -- Processes multiple aggregation pipelines within a single stage.
$geoNear -- Returns documents sorted by proximity to a specified point.
$group -- Groups documents by a specified identifier and performs accumulations.
$lookup -- Performs a left outer join with another collection.
$merge -- Writes the results of an aggregation pipeline to a specified collection.
$project -- Reshapes each document in the stream, including or excluding fields.
$replaceRoot -- Replaces the input document with the specified document.
$sample -- Randomly selects documents from a collection.
$sort -- Sorts documents based on specified fields.
$unwind -- Deconstructs an array field from the input documents to output a document for each element.