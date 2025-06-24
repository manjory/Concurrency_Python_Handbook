import threading
import queue
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(threadName)s: %(message)s")
q = queue.Queue(maxsize=5)

def producer(n):
    for i in range(n):
        q.put(i)
        logging.info(f"Produced {i}")
        time.sleep(0.1)
    # signal consumers to exit
    for _ in range(2):
        q.put(None)

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        logging.info(f"Consumed {item}")
        q.task_done()

if __name__ == "__main__":
    n = 10
    producers = [threading.Thread(target=producer, args=(n,))]
    consumers = [threading.Thread(target=consumer) for _ in range(2)]
    for t in producers + consumers:
        t.start()
    for t in producers:
        t.join()
    q.join()
    for t in consumers:
        t.join()
