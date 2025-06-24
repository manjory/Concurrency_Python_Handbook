import threading
import time


class BorkenCounter:
    def __init__(self):
        self.value=0

    def  increment(self):
        temp= self.value
        print(f"[{threading.current_thread().name}] Read value: {temp}")
        time.sleep(0.00001)
        temp+=1
        self.value = temp
        print(f"[{threading.current_thread().name}] Wrote value: {self.value}")

def run_increment(counter: BorkenCounter, times):
    for _ in range(times):
        counter.increment()

if __name__=="__main__":
    counter= BorkenCounter()

    num_threads= 5
    increments_per_thread= 100000

    threads = []

    for _ in range(num_threads):
        t= threading.Thread(target = run_increment, args=(counter,increments_per_thread))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print(f"Expected : {num_threads*increments_per_thread}")
    print(f"Got : {counter.value}")
