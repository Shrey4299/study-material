import queue
import threading
import time

# ********************************************** Creating Threads: **********************************************


# Define a function for the thread
def print_numbers():
    for i in range(10):
        time.sleep(1)
        print(i)


# Create a thread object
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("Thread has finished execution")

# ********************************************** Thread Synchronization: **********************************************
counter = 0
counter_lock = threading.Lock()
def increment_counter():
    global counter
    for _ in range(100000):
        with counter_lock:
            counter += 1
# Create two threads to increment the counter
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)
# Start the threads
thread1.start()
thread2.start()
# Wait for both threads to finish
thread1.join()
thread2.join()
print("Final counter value:", counter)


# ********************************************** Thread Communication: **********************************************

def producer(q):
    for i in range(5):
        q.put(i)


def consumer(q):
    while True:
        data = q.get()
        if data is None:
            break
        print("Consumed:", data)


# Create a shared queue
shared_queue = queue.Queue()
# Create producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(shared_queue,))
consumer_thread = threading.Thread(target=consumer, args=(shared_queue,))
# Start the threads
producer_thread.start()
consumer_thread.start()
# Wait for the producer to finish
producer_thread.join()
# Add a sentinel value to signal the consumer to exit
shared_queue.put(None)
# Wait for the consumer to finish
consumer_thread.join()
