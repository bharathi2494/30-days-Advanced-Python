# gil_thread_demo.py
# Demonstrates Global Interpreter Lock (GIL)

import threading
import time

def cpu_task():
    count = 0
    for _ in range(10_000_000):
        count += 1

start = time.time()

t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Time taken with threads: {end - start:.2f} seconds")
