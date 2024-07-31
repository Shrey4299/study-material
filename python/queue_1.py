import queue

# Create a FIFO queue
q = queue.Queue()

# Add items to the queue
q.put("first")
q.put("second")
q.put("third")

# Retrieve items from the queue
while not q.empty():
    item = q.get()
    print(item)
