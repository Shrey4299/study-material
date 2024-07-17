import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or select database
db = client["ecommerce"]

# Create or select collections
user_collection = db["user"]
product_collection = db["product"]

# Insert sample data into the user collection
# users_data = [
#     {"name": "Alice", "email": "alice@example.com", "age": 30},
#     {"name": "Bob", "email": "bob@example.com", "age": 25},
#     {"name": "Charlie", "email": "charlie@example.com", "age": 35},
# ]
# user_collection.insert_many(users_data)

# # Insert sample data into the product collection
# products_data = [
#     {"name": "Laptop", "price": 1000},
#     {"name": "Smartphone", "price": 500},
#     {"name": "Headphones", "price": 50},
# ]
# product_collection.insert_many(products_data)


# ################ Simple INSERT queries ###############
# user_data = {"username": "alice123", "isAdmin": True}
# user_insert_result = user_collection.insert_one(user_data)
# print(user_insert_result.inserted_id)


# Fetch all documents from the user collection
# users = user_collection.find()
# print("Users:")
# for user in users:
#     print(user)

# # Fetch all documents from the product collection
# products = product_collection.find()
# print("\nProducts:")
# for product in products:
#     print(product)


# Fetch Single User from the user collection
# user = user_collection.find_one({"username": "alice123"})
# print(user , "single user")


# Fetch All Users with some conditions
# users_with_specific_fields = list(
#     user_collection.find({}, {"name": "alice123" , "age": "35"})
# )
# print("Users with specific fields:")
# print(users_with_specific_fields)

# products = list(product_collection.find({}))
# print(products)


# products = list(product_collection.find({}, {"name": "Laptop"}))
# print(products)

# product_with_operator_example = list(
#     product_collection.find(
#         {
#             "$or": [
#                 {"price": {"$lt": 1000, "$eq": None}},
#                 {
#                     "$or": [
#                         {"name": {"$regex": "^Boat"}},
#                         {"quantity": {"$gt": "40"}},
#                     ]
#                 },
#             ]
#         }
#     )
# )

# posts_with_operators = list(
#     post_collection.find(
#         {
#             "$and": [{"a": 5}, {"b": 6}],
#             "$or": [{"a": 5}, {"b": 6}],
#             "someAttribute": {
#                 "$eq": 3,
#                 "$ne": 20,
#                 "$exists": True,
#                 "$exists": False,
#                 "$in": [5, 6],
#                 "$gt": 6,
#                 "$gte": 6,
#                 "$lt": 10,
#                 "$lte": 10,
#                 "$nin": [1, 2],
#                 "$regex": "hat",
#                 "$options": "i",
#             },
#         }
#     )
# )

# print(product_with_operator_example)

# ################ Simple UPDATE queries ###############
# Change everyone without a last name to "Doe"
# user_collection.update_many({"name": "Bob"}, {"$set": {"name": "shrey"}})


# ################ Simple DELETE queries ###############
# Delete everyone named "Jane"
# user_collection.delete_many({"name": "Jane"})

# ################ Grouping ###############
# Equivalent to GROUP BY name
# projects_grouped_by = list(
#     client["test_db"]["project"].aggregate([{"$group": {"_id": "$name"}}])
# )

# ################ Limits and Pagination ###############
# Skip 5 instances and fetch the next 5
# products_paginated = list(product_collection.find().skip(1).limit(2))
# print(products_paginated)

# ################ max, min, and sum ###############
# max_age = user_collection.find().sort("age", pymongo.DESCENDING).limit(1)
# min_age = user_collection.find().sort("age", pymongo.ASCENDING).limit(1)
# Aggregate to get the sum of ages
# sum_of_ages_cursor = user_collection.aggregate(
#     [{"$group": {"_id": None, "total": {"$sum": "$age"}}}]
# )

# # Extract and print the result
# sum_of_ages_result = list(sum_of_ages_cursor)
# print("Sum of ages:", sum_of_ages_result[0]["total"] if sum_of_ages_result else 0)

# ################ increment, decrement ###############
# user_collection.update_one({"_id": 1}, {"$inc": {"age": 5}})
# user_collection.update_one({"_id": 1}, {"$inc": {"age": -5}})

# ################ count ###############
# count_by_status = list(
#     client["test_db"]["lead"].aggregate(
#         [{"$group": {"_id": "$status", "count": {"$sum": 1}}}]
#     )
# )
