#Create 2 threads and join the threads
"""
1. Write multithreaded function to implement a critical section and show the case of critical section
2. Write a function to add monitors/locks/semaphore to prevent race condition on critical section
3. create a function to implement 2 methods reaching out used by 2 threads with same variable used in both methods
and both method updating the same variable.
4. implement all kinds of locks read/write, re-interrant locks
5. difference between async and concurrency and write a code to show the diff and similarity between the two. PRint them
6. WAP to do a multiprocessing of create a process. End the process and also create a race condition between the process.
7. Implement a deadlock(necessary and sufficient conditions for deadlock). show necessary and sufficient condition via tests
8. Implement a Bezantine General's problem
9. How to build consensus on a multiprocessing system
10. What is causality
11. Use futures in asyncio
12. What are the two paradigms in ashncio
"""
import threading
import time


# Subclass threading.Thread and override run() → more like a Runner (Java-style).

class MyThread(threading.Thread):
    def run(self):
        return self.run_something()

    def run_something(self):
        print("something")
        time.sleep(2)
        print("DONE")

if __name__=="__main__":
    thread_handler = MyThread()
    print("starting")
    thread_handler.start()
    print("started")
    thread_handler.join()
    print("JOINED")






