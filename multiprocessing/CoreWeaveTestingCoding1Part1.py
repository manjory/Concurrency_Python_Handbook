"""
1. How would you make the something_slow function run in 1 sec if its called 10 times from main()

"""
import sys
import time
import multiprocess

def something_slow(job_id: int) -> None:
    print(f"starting job {job_id}")
    time.sleep(1)
    print(f"completed job {job_id}")


def main() -> None:
    # queue = multiprocessing.Queue()
    processes = []

    for i in range(10):
        process = multiprocess.Process(target=something_slow, args=(i,))
        processes.append(process)
        process.start()
        process.join()

    # Collect results from queue


if __name__ == "__main__":
    sys.exit(main())
