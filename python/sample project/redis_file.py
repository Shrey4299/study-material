# redis_demo.py

import redis

# Connect to a local Redis server
r = redis.Redis(host="localhost", port=6379, db=0)

# Basic key operations
r.set("key", "value")
print(f'Key "key" value: {r.get("key")}')

# Strings
r.set("string_key", "Hello, Redis!")
print(f'String key value: {r.get("string_key")}')

# Hashes
r.hset("hash_key", "field1", "value1")
r.hset("hash_key", "field2", "value2")
print(f'Hash key fields: {r.hkeys("hash_key")}')
print(f'Hash key values: {r.hvals("hash_key")}')

# Lists
r.rpush("list_key", "item1")
r.rpush("list_key", "item2")
print(f'List key values: {r.lrange("list_key", 0, -1)}')

# Sets
r.sadd("set_key", "item1")
r.sadd("set_key", "item2")
print(f'Set key values: {r.smembers("set_key")}')

# Sorted sets
r.zadd("sorted_set_key", {"item1": 1, "item2": 2})
print(f'Sorted set key values: {r.zrange("sorted_set_key", 0, -1, withscores=True)}')

# Pub/Sub

# Subscribe to a channel
sub = redis.Redis(host="localhost", port=6379, db=0)
psub = sub.pubsub()
psub.psubscribe("channel_name")

# Publish a message to a channel
r.publish("channel_name", "Hello, Redis!")

# Receive published messages
for message in psub.listen():
    print(f"Received message: {message}")
