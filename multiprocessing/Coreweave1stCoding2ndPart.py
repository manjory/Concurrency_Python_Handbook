"""1. collect results in main from something slow
2. Print it
"""

import sys
import time
import multiprocess

def something_slow(job_id) -> str:
    print(f"starting job {job_id}")
    time.sleep(1)
    print(f"completed job {job_id}")
    return "SUCCESS"
def wrapper(job_id,queue: multiprocess.Queue):
    result=something_slow(job_id)
    queue.put(result)

def main() -> None:
    queue = multiprocess.Queue()
    processes = []
    start_time=time.time()
    for i in range(10):
        process = multiprocess.Process(target=wrapper, args=(i,queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
    end_time=time.time()

    results=[]

    while not queue.empty():
        results.append(queue.get())
    print("RESULTS:: ",results)
    print("total time taken==", end_time-start_time," seconds")
    # Collect results from queue


if __name__ == "__main__":
    sys.exit(main())
