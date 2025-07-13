"""
Counting Semaphore (threading.Semaphore)
🔸 Problem Statement: Parking Lot with Limited Spots
Simulate a parking lot with 3 parking spots. Create 6 car threads. Each car tries to enter the parking lot, stays for a second, then leaves. Use a Semaphore(3) to limit concurrent access. Cars that can't enter should wait until a spot is free.

✅ Focus: Counting semaphore as a limiter for concurrent thread access.

"""
