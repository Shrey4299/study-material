import redis
from redis.commands.json.path import Path
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

# Connect to your Redis database
r = redis.Redis(host="localhost", port=6379)

# Create some test data to add to your database
user1 = {
    "name": "Paul John",
    "email": "paul.john@example.com",
    "age": 42,
    "city": "London",
}
user2 = {
    "name": "Eden Zamir",
    "email": "eden.zamir@example.com",
    "age": 29,
    "city": "Tel Aviv",
}
user3 = {
    "name": "Paul Zamir",
    "email": "paul.zamir@example.com",
    "age": 35,
    "city": "Tel Aviv",
}

# Define indexed fields and their data types using schema
schema = (
    TextField("$.name", as_name="name"),
    TagField("$.city", as_name="city"),
    NumericField("$.age", as_name="age"),
)

# Create an index
rs = r.ft("idx:users")
rs.create_index(
    schema, definition=IndexDefinition(prefix=["user:"], index_type=IndexType.JSON)
)

# Use JSON.SET to set each user value at the specified path
r.json().set("user:1", Path.root_path(), user1)
r.json().set("user:2", Path.root_path(), user2)
r.json().set("user:3", Path.root_path(), user3)

# Find user Paul and filter the results by age
res = rs.search(Query("Paul @age:[30 40]"))
print(res)

# Query using JSON Path expressions
res = rs.search(Query("Paul").return_field("$.city", as_field="city")).docs
print(res)

# Aggregate your results using FT.AGGREGATE
req = aggregations.AggregateRequest("*").group_by(
    "@city", reducers.count().alias("count")
)
print(rs.aggregate(req).rows)
