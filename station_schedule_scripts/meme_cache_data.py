from pymemcache.client import base

# Connect to Memcached
client = base.Client(("localhost", 11211))

# Step 1: Set some key-value pairs
client.set("key1", "value1")
client.set("key2", "value2")
client.set("key3", "value3")
print("Values set in Memcached.")

# Clear all data in Memcached
client.flush_all()
print("All data in Memcached has been cleared.")

# Step 2: Retrieve all values (should be empty)


def get_all_keys(client):
    items = client.stats("items")
    keys = []
    for item in items:
        if "items:" in item:
            parts = item.split(":")
            if len(parts) > 2 and parts[2] == "number":
                slab_id = parts[1]
                limit = int(items[item])
                cachedump = client.stats("cachedump", slab_id, limit)
                keys.extend(cachedump.keys())
    return keys


def get_all_values(client, keys):
    values = {}
    for key in keys:
        values[key] = client.get(key)
    return values


# Fetch all keys (should be empty after flush)
keys = get_all_keys(client)

# Fetch all values based on the keys (should be empty after flush)
values = get_all_values(client, keys)

# Print all values (should print nothing)
if not values:
    print("No values found in Memcached.")
else:
    for key, value in values.items():
        print(f"{key}: {value}")
