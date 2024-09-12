Basic MongoDB Shell Commands

<!-- ******************************************************************************************************************************** -->
1. Show Databases:
show dbs

2. Switch to a Database:
use <database_name>
Note: If the database does not exist, it will be created.

3. Show Collections in a Database:
show collections
Example:
db.createCollection("posts")

<!-- ******************************************************************************************************************************** -->


Insert Documents into a Collection:

4. Insert One Document:
db.collection.insert({ key: 'value', key2: 'value2' })

5. Insert One Document with Specific Data:
db.posts.insertOne({
  title: "Post Title 1",
  body: "Body of post.",
  category: "News",
  likes: 1,
  tags: ["news", "events"],
  date: Date()
})

6. Insert Multiple Documents:
db.posts.insertMany([
  { title: "Post Title 2", body: "Body of post 2.", category: "Tech", likes: 3, tags: ["tech"], date: Date() },
  { title: "Post Title 3", body: "Body of post 3.", category: "Health", likes: 5, tags: ["health"], date: Date() }
])

7. Insert and validating the schema
db.createCollection("posts", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: [ "title", "body" ],
      properties: {
        title: {
          bsonType: "string",
          description: "Title of post - Required."
        },
        body: {
          bsonType: "string",
          description: "Body of post - Required."
        },
        category: {
          bsonType: "string",
          description: "Category of post - Optional."
        },
        likes: {
          bsonType: "int",
          description: "Post like count. Must be an integer - Optional."
        }
      }
    }
  }
})

<!-- ******************************************************************************************************************************** -->


Query Documents:

- Find All Documents:
db.collection.find()

- Find the First Document:
db.posts.findOne()

- Find Documents with a Query:
db.collection.find({ key: 'value' })

- Exclude Certain Fields:
db.posts.find({}, { _id: 0, title: 1, date: 1 })
Note: You cannot use both 0 and 1 in the same object, except for the _id field. Specify fields to include or exclude, but not both.

<!-- ******************************************************************************************************************************** -->


Update Documents:

- Update a Document:
db.collection.update({ key: 'value' }, { $set: { key2: 'new_value' } })

- Insert if Document Not Found (Upsert):
db.posts.updateOne(
  { title: "Post Title 5" },
  {
    $set: {
      title: "Post Title 5",
      body: "Body of post.",
      category: "Event",
      likes: 5,
      tags: ["news", "events"],
      date: Date()
    }
  },
  { upsert: true }
)

Update Multiple Documents:
db.posts.updateMany({}, { $inc: { likes: 1 } })

<!-- ******************************************************************************************************************************** -->


Delete Documents:

- Delete a Single Document:
db.collection.remove({ key: 'value' })
Example:
db.posts.deleteOne({ title: "Post Title 5" })

- Delete Multiple Documents:
db.posts.deleteMany({ category: "Technology" })


<!-- ******************************************************************************************************************************** -->


Count Documents in a Collection:
db.collection.countDocuments()

<!-- ******************************************************************************************************************************** -->


Drop a Collection:
db.collection.drop()

Drop a Database:
db.dropDatabase()
