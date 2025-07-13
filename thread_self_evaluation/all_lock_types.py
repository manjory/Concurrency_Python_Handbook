"""
1. Mutex (Mutual Exclusion Lock):
What it does: Allows only one thread/process to access a resource at a time.


lock = threading.Lock()
with lock:
    # critical section

2. Reentrant Lock (RLock)
What it does: A thread can acquire it multiple times without blocking itself.

lock = threading.RLock()
lock.acquire()
lock.acquire()
lock.release()
lock.release()

3. Semaphore
What it does: Controls access to a resource pool with n slots (vs just one in a lock).

sem = threading.Semaphore(3)
sem.acquire()
# do something
sem.release()


4. Bounded Semaphore
A version of Semaphore with a limit on how many times it can be released.

Prevents bugs from over-releasing.


5. Condition
What it does: Wait for a condition to be met before continuing (uses a lock underneath).
condition = threading.Condition()

with condition:
    condition.wait()       # Wait until notified
    # do something
    condition.notify_all() # Wake up all waiting threads


6. Event
What it does: A flag that threads can wait for.

event = threading.Event()

def wait_for_event():
    event.wait()  # Blocks until event is set

event.set()       # Releases all waiting threads


7. Barrier
What it does: Synchronizes a fixed number of threads to reach a point before any proceeds.


Python: threading.Barrier(parties)
"""
