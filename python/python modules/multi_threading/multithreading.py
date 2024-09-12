import os
from multiprocessing.pool import ThreadPool
from multiprocessing import cpu_count
from PIL import Image
import requests
from io import BytesIO
import time

# Function to download an image and return its size
def get_size_img(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        size = img.size
        print(f"Processed image from {url}: Size {size}")
        return size
    except Exception as e:
        print(f"Failed to process image from {url}: {e}")
        return None

# List of image URLs to process
response_data = [
    "https://via.placeholder.com/150",
    "https://via.placeholder.com/200",
    "https://via.placeholder.com/250",
    "https://via.placeholder.com/300",
    "https://via.placeholder.com/350",
    "https://via.placeholder.com/400",
]

# Determine the number of CPUs (optional)
cpus = cpu_count()
print(f"Number of CPUs available: {cpus}")

# Start timing
start_time = time.time()

# Using ThreadPool to process images in parallel
with ThreadPool(12) as pools:  # Adjust the number of threads as needed
    results = pools.map(get_size_img, response_data)
    pools.close()

# Stop timing
end_time = time.time()

# Displaying the results
print("All image sizes:", results)

# Print the execution time
execution_time = end_time - start_time
print(f"Execution Time: {execution_time:.2f} seconds")
