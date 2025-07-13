"""
 Write multithreaded function to implement a critical section and show the case of critical section
"""
import threading
from threading import Thread,Lock

"""
CRITICAL SECTION problem is solved using 2 general approaches:
1. Per-emptive kernels: It allows the process to be preemted while running in the kernel mode. This comes as a better option with a good Kernel code design
as it allows for switching actions to different process that might need the same resource, but inherently doesnt prevent race condition 
for processes running in concurrent manner.
2. Nonpreemptive kernels:  in this mode the Nonpreemptive kernel does not allow a process running in kernel mode to be preempted. A kernel mode process
will run until it exits the kernel mode, blocks or voluntarily yields control of the CPU. Inherently solves the race condition problems, 
but runs the risk of hogging the CPU for significantly long time
    
"""
mutex=Lock()

parkingSpace=10
def test_and_set(numCars):
    global parkingSpace
    mutex.acquire()
    try:
        parkingSpace= parkingSpace + numCars
        print("total number of cars in parking space", parkingSpace)
    finally:
        mutex.release()





if __name__ == "__main__":
    n=10
    threads=[]
    for i in range(n):
        thread_handler= threading.Thread(target=test_and_set,args=(2,))
        thread_handler.start()
        threads.append(thread_handler)
        print("\nhandler done")
    for t in thread_handler:
        t.join()



# add a number and print the number before and after. with thread id and thread name, exit
# wap to add a number to critical section before and after update with thread id
