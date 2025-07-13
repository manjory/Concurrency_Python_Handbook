"""
 Problem Statement: Nested Logging System
Create a thread-safe logging class SafeLogger that writes to a shared log file. The log() method internally calls two other methods: write_header() and write_message(). All three methods should acquire the same RLock, since they are nested calls. Start 3 threads, each calling log() 5 times.

✅ Focus: Demonstrate why RLock is needed when recursive or nested locking is involved.

"""
