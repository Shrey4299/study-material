MongoDB Indexing and Search Operations

Indexing

Create an Index:

db.collection.createIndex({ field: 1 }) (Ascending index)
db.collection.createIndex({ field: -1 }) (Descending index)
Create a Compound Index:

db.collection.createIndex({ field1: 1, field2: -1 })
Create a Text Index:

db.collection.createIndex({ field: "text" })
Create a Geospatial Index:

db.collection.createIndex({ location: "2dsphere" })
Create a Hashed Index:

db.collection.createIndex({ field: "hashed" })
List All Indexes:

db.collection.getIndexes()
Drop an Index:

db.collection.dropIndex("index_name")
Drop All Indexes:

db.collection.dropIndexes()
Search

Basic Query:

db.collection.find({ field: value })
Query with Projection:

db.collection.find({ field: value }, { fieldToInclude: 1 })
Text Search:

db.collection.find({ $text: { $search: "search_term" } })
Text Search with Score:

db.collection.find({ $text: { $search: "search_term" } }, { score: { $meta: "textScore" } }).sort({ score: { $meta: "textScore" } })


db.collection.find({ field: { $regex: /pattern/, $options: "i" } })
Find with $exists:

db.collection.find({ field: { $exists: true } })


examples:

db.movies.aggregate([
  {
    $search: {
      index: "default", // optional unless you named your index something other than "default"
      text: {
        query: "star wars",
        path: "title"
      },
    },
  },
  {
    $project: {
      title: 1,
      year: 1,
    }
  }
])


