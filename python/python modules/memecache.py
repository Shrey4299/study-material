import memcache
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Create a Memcached client with specific configuration
cache_client = memcache.Client(
    ["127.0.0.1:11211"], server_max_value_length=1024 * 1024 * 50
)


# Set a value in the cache
def set_value(key, value):
    result = cache_client.set(key, value)
    if result:
        logging.info(f"Successfully set {key} = {value}")
    else:
        logging.error(f"Failed to set {key}")


# Get a value from the cache
def get_value(key):
    value = cache_client.get(key)
    if value:
        logging.info(f"Successfully retrieved {key} = {value}")
    else:
        logging.error(f"{key} not found in cache")
    return value


# Delete a value from the cache
def delete_value(key):
    result = cache_client.delete(key)
    if result:
        logging.info(f"Successfully deleted {key}")
    else:
        logging.error(f"Failed to delete {key}")


# Example usage
if __name__ == "__main__":
    # Set values
    set_value("foo", "bar")
    set_value("number", 42)

    # Get values
    get_value("foo")
    get_value("number")

    # Delete a value
    delete_value("foo")

    # Try to get a deleted value
    get_value("foo")



# Certainly! Here's a concise guide for installing Memcached and using it on Linux:

# plaintext
# Copy code
# # Memcached Installation and Basic Usage Guide for Linux

# ## Installation

# ### Debian/Ubuntu

# 1. Update the package list:
#    ```bash
#    sudo apt update
# Install Memcached and the associated tools:

# bash
# Copy code
# sudo apt install memcached libmemcached-tools
# Start and enable the Memcached service:

# bash
# Copy code
# sudo systemctl start memcached
# sudo systemctl enable memcached
# Check the status to ensure it is running:

# bash
# Copy code
# sudo systemctl status memcached
# Basic Usage
# Using Telnet (Direct Interaction)
# Open a terminal and connect to Memcached:

# bash
# Copy code
# telnet localhost 11211
# Set a value:

# arduino
# Copy code
# set mykey 0 900 7
# myvalue
# Retrieve the value:

# arduino
# Copy code
# get mykey
# Delete the value:

# arduino
# Copy code
# delete mykey