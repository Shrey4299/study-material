const mongoose = require("mongoose");
const { Schema } = mongoose;

// Define a Mongoose schema for the 'User' model
const userSchema = new Schema({
  username: String,
  isAdmin: Boolean,
});

// Create a Mongoose model based on the schema
const User = mongoose.model("User", userSchema);

// ################ Simple INSERT queries ###############

const user = await User.create({
  username: "alice123",
  isAdmin: true,
});
// let's assume the default of isAdmin is false
console.log(user.username); // 'alice123'
console.log(user.isAdmin); // false

// ################ Simple SELECT queries ###############

const users = await User.find();

User.find({}, { foo: 1, bar: 1 });
// Equivalent to SELECT foo, bar FROM ...

User.find({}, { foo: 1, bar: 1, _id: 0 });
// Equivalent to SELECT foo, bar FROM ... (excluding _id field)

User.find({}, { foo: 1, bar: 1, hats: { $size: "$hats" } });
// Equivalent to SELECT foo, bar, COUNT(hats) AS n_hats FROM ...

// ################ Applying WHERE clauses ###############

const posts = await Post.find({ authorId: 2 });
// Equivalent to SELECT * FROM post WHERE authorId = 2;

const { $and, $or } = mongoose.mongo;
const postsWithAndCondition = await Post.find({
  $and: [{ authorId: 12 }, { status: "active" }],
});
// Equivalent to SELECT * FROM post WHERE authorId = 12 AND status = 'active';

const postsWithOrCondition = await Post.find({
  $or: [{ authorId: 12 }, { authorId: 13 }],
});
// Equivalent to SELECT * FROM post WHERE authorId = 12 OR authorId = 13;

// ################ Operators ###############

const postsWithOperators = await Post.find({
  $and: [{ a: 5 }, { b: 6 }], // (a = 5) AND (b = 6)
  $or: [{ a: 5 }, { b: 6 }], // (a = 5) OR (b = 6)
  someAttribute: {
    // Basics
    $eq: 3, // = 3
    $ne: 20, // != 20
    $exists: true, // IS NOT NULL
    $exists: false, // IS NULL
    $or: [5, 6], // (someAttribute = 5) OR (someAttribute = 6)

    // Number comparisons
    $gt: 6, // > 6
    $gte: 6, // >= 6
    $lt: 10, // < 10
    $lte: 10, // <= 10
    $in: [1, 2], // IN [1, 2]
    $nin: [1, 2], // NOT IN [1, 2]

    // String comparisons
    $regex: /hat/, // LIKE '%hat%'
    $options: "i", // Case-insensitive
  },
});

// ################ Operator Example ###############

const foosWithOperatorExample = await Foo.find({
  $or: [
    {
      rank: {
        $lt: 1000,
        $eq: null,
      },
    },
    {
      $or: [{ title: { $regex: /^Boat/ } }, { description: { $regex: /boat/ } }],
    },
  ],
});

// ################ Simple UPDATE queries ###############

// Change everyone without a last name to "Doe"
await User.updateMany({ lastName: null }, { $set: { lastName: "Doe" } });

// ################ Simple DELETE queries ###############

// Delete everyone named "Jane"
await User.deleteMany({ firstName: "Jane" });

// ################ Creating in bulk ###############

const captains = await Captain.insertMany([{ name: "Jack Sparrow" }, { name: "Davy Jones" }]);

// ################ Grouping ###############

const projectsGroupedBy = await Project.aggregate([{ $group: { _id: "$name" } }]);
// Equivalent to GROUP BY name

// ################ Limits and Pagination ###############

// Skip 5 instances and fetch the 5 after that
const projectsPaginated = await Project.find().skip(5).limit(5);

// ################ max, min, and sum ###############

const maxAge = await User.find().max("age");
// Equivalent to SELECT MAX(age) as age FROM User

const minAge = await User.find().min("age");
// Equivalent to SELECT MIN(age) as age FROM User

const sumOfAges = await User.find().sum("age");
// Equivalent to SELECT SUM(age) as age FROM User

// ################ increment, decrement ###############

await User.updateOne({ _id: 1 }, { $inc: { age: 5 } });
// Will increase age to 5

await User.updateOne({ _id: 1 }, { $inc: { age: -5 } });
// Will decrease age to 5

// ################ count ###############

const countByStatus = await Lead.aggregate([{ $group: { _id: "$status", count: { $sum: 1 } } }]);
// Equivalent to SELECT status, COUNT(*) as count FROM Lead GROUP BY status
