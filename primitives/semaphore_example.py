"""
References:
https://www.delftstack.com/howto/python/python-semaphore/
https://www.pythontutorial.net/python-concurrency/python-semaphore/
"""

import logging
import threading
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(threadName)s ]%(message)s")

semaphore = threading.Semaphore(2)

def worker(task_id):
    logging.info(f"Task {task_id} waiting to enter")

    with semaphore:
        logging.info(f"Task {task_id} entering critical section")
        time.sleep(1)
        logging.info(f"Task {task_id} leaving critical section")

if __name__=="__main__":
    threads= [threading.Thread(target=worker,args=(i,)) for i in range(5)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()


