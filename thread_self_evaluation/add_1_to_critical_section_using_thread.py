"""(READ/WRITE lock)
1. Write a function to implement critical section. This function should have three actions .
i). Print the number it’s acting on with the thread ID.
ii). Add 1 to the number. And,
iii). Print the number after updating with its thread ID
2. Use a function call This method from two different time threads 10 times each
currect implementation expects 21 in response
"""
import threading
from threading import Lock

mutex=Lock()
shared_number=1

def critical_section(thread_id):
    global shared_number
    mutex.acquire()
    print("number: ",shared_number," thread_id :",thread_id)
    shared_number+=1
    print("number: ",shared_number," thread_id :",thread_id)
    mutex.release()
    # return number

def call_function(thread_id):
    # number=1
    for i in range(10):
        critical_section(thread_id)

if __name__ == "__main__":
    thread1=threading.Thread(target=call_function, args=("thread_1",))
    thread2=threading.Thread(target=call_function,args=("thread_2",))
    print("thread_1 action start")
    thread1.start()
    print("thread_2 action start")
    thread2.start()
    thread1.join()
    print("thread_1 action ended")
    thread2.join()
    print("thread_2 action ended")






