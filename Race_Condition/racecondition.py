import threading
import time

counter = 0

def increment_counter():
    global counter
    for _ in range(100000):
        # Simulate some work
        time.sleep(0.001)
        # Increment the counter
        counter += 3

t1 = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=increment_counter)

t1.start()
t2.start()

t1.join()
t2.join()

print("Nilai counter:", counter)