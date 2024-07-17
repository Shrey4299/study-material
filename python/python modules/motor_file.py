import asyncio
import motor.motor_asyncio

# Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")

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
# await user_collection.insert_many(users_data)

# # Insert sample data into the product collection
# products_data = [
#     {"name": "Laptop", "price": 1000},
#     {"name": "Smartphone", "price": 500},
#     {"name": "Headphones", "price": 50},
# ]
# await product_collection.insert_many(products_data)


################ Simple INSERT queries ###############
# user_data = {"username": "alice123", "isAdmin": True}
# user_insert_result = await user_collection.insert_one(user_data)
# print(user_insert_result.inserted_id)


# Fetch all documents from the user collection
# users = await user_collection.find().to_list(None)
# print("Users:")
# for user in users:
#     print(user)

# # Fetch all documents from the product collection
# products = await product_collection.find().to_list(None)
# print("\nProducts:")
# for product in products:
#     print(product)


# Fetch Single User from the user collection
# user = await user_collection.find_one({"username": "alice123"})
# print(user , "single user")


# Fetch All Users with some conditions
# users_with_specific_fields = await user_collection.find(
#     {}, {"name": "alice123" , "age": "35"}
# ).to_list(None)
# print("Users with specific fields:")
# print(users_with_specific_fields)

# products = await product_collection.find().to_list(None)
# print(products)


# products = await product_collection.find({}, {"name": "Laptop"}).to_list(None)
# print(products)

# product_with_operator_example = await product_collection.find(
#     {
#         "$or": [
#             {"price": {"$lt": 1000, "$eq": None}},
#             {
#                 "$or": [
#                     {"name": {"$regex": "^Boat"}},
#                     {"quantity": {"$gt": "40"}},
#                 ]
#             },
#         ]
#     }
# ).to_list(None)

# posts_with_operators = await post_collection.find(
#     {
#         "$and": [{"a": 5}, {"b": 6}],
#         "$or": [{"a": 5}, {"b": 6}],
#         "someAttribute": {
#             "$eq": 3,
#             "$ne": 20,
#             "$exists": True,
#             "$exists": False,
#             "$in": [5, 6],
#             "$gt": 6,
#             "$gte": 6,
#             "$lt": 10,
#             "$lte": 10,
#             "$nin": [1, 2],
#             "$regex": "hat",
#             "$options": "i",
#         },
#     }
# ).to_list(None)

# print(product_with_operator_example)

# ################ Simple UPDATE queries ###############
# Change everyone without a last name to "Doe"
# await user_collection.update_many({"name": "Bob"}, {"$set": {"name": "shrey"}})


# ################ Simple DELETE queries ###############
# Delete everyone named "Jane"
# await user_collection.delete_many({"name": "Jane"})

# ################ Grouping ###############
# Equivalent to GROUP BY name
# projects_grouped_by = await client["test_db"]["project"].aggregate([{"$group": {"_id": "$name"}}]).to_list(None)

# ################ Limits and Pagination ###############
# Skip 5 instances and fetch the next 5
# products_paginated = await product_collection.find().skip(1).limit(2).to_list(None)
# print(products_paginated)

# ################ max, min, and sum ###############
# max_age = await user_collection.find().sort("age", pymongo.DESCENDING).limit(1).to_list(None)
# min_age = await user_collection.find().sort("age", pymongo.ASCENDING).limit(1).to_list(None)
# Aggregate to get the sum of ages
# sum_of_ages_cursor = user_collection.aggregate(
#     [{"$group": {"_id": None, "total": {"$sum": "$age"}}}]
# )

# # Extract and print the result
# sum_of_ages_result = await sum_of_ages_cursor.to_list(None)
# print("Sum of ages:", sum_of_ages_result[0]["total"] if sum_of_ages_result else 0)

# ################ increment, decrement ###############
# await user_collection.update_one({"_id": 1}, {"$inc": {"age": 5}})
# await user_collection.update_one({"_id": 1}, {"$inc": {"age": -5}})

# ################ count ###############
# count_by_status = await client["test_db"]["lead"].aggregate(
#     [{"$group": {"_id": "$status", "count": {"$sum": 1}}}]
# ).to_list(None)


# import asyncio
# from motor.motor_asyncio import AsyncIOMotorClient
# from pymongo.server_api import ServerApi


# async def ping_server():
#     # Replace the placeholder with your Atlas connection string
#     uri = "mongodb://localhost:27017/"

#     # Set the Stable API version when creating a new client
#     client = AsyncIOMotorClient(uri, server_api=ServerApi("1"))

#     # Send a ping to confirm a successful connection
#     try:
#         await client.admin.command("ping")
#         print("Pinged your deployment. You successfully connected to MongoDB!")
#     except Exception as e:
#         print(e)


# asyncio.run(ping_server())
