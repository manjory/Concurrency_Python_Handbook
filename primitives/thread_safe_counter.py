import threading

class ThreadSafeCounter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value+=1

    def get(self):
        with self.lock:
            return self.value


def run_increment(counter: ThreadSafeCounter, times: int):
    for _ in range(times):
        counter.increment()

if __name__=="__main__":
    counter= ThreadSafeCounter()
    num_threads=5

    increments_per_thread=100000

    threads=[]

    for _ in range(num_threads):
        t= threading.Thread(target=run_increment,args = (counter, increments_per_thread))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Expected:{num_threads*increments_per_thread}")
    print(f"Got :{counter.get()}")
