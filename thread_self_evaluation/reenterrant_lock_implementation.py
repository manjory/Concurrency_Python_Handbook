"""
 Problem Statement: Nested Logging System
Create a thread-safe logging class SafeLogger that writes to a shared log file.
The log() method internally calls two other methods: write_header() and write_message().
All three methods should acquire the same RLock, since they are nested calls.
Start 3 threads, each calling log() 5 times.

✅ Focus: Demonstrate why RLock is needed when recursive or nested locking is involved.

"""
import threading


class SafeLogger:
    def __init__(self):
        self.lock=threading.RLock()
        self.log_file={}

    def write_header(self,header):
        self.log_file[header]=[]


    def write_message(self,header,message):
        self.log_file[header].append(message)
    def log(self, log):
        with self.lock:
            header=log["header"]["timestamp"]
            message=log["message"]
            self.write_header(header)
            self.write_message(header,message)

if __name__=="__main__":
    logger=SafeLogger()
    logMessage = [{"header": {"timestamp":"2024-07-15 10:35:00"}, "message": "Application started"}, {"header":{"timestamp":"2024-07-15 10:30:00"}, "message": "Error: Database connection failed"}, {"header": {"timestamp": "2024-07-15 10:40:00"}, "message": "Error: Third attempt failed"}]
    # thread1 =threading.Thread(target=logger.log, args=(logMessage[0],))
    # thread2 =threading.Thread(target=logger.log, args=(logMessage[1],))
    # thread3 =threading.Thread(target=logger.log, args=(logMessage[2],))

    threads=[]
    for i in range(5):
        thread1 =threading.Thread(target=logger.log, args=(logMessage[0],))
        thread2 =threading.Thread(target=logger.log, args=(logMessage[1],))
        thread3 =threading.Thread(target=logger.log, args=(logMessage[2],))
        threads.extend([thread1,thread2, thread3])
        thread1.start()
        thread2.start()
        thread3.start()
    for thread in threads:
        thread.join()

    print("\nFinal log file:")
    for header, messages in logger.log_file.items():
        print("header",header,"-->","message", messages)









