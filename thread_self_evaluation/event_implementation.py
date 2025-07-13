"""
Event
🔸 Problem Statement: Launch Countdown Control
Simulate a rocket launch system where the main thread waits for 3 system checks (threads) to complete before proceeding. Each system check calls event.set() once done. The main thread should call event.wait() to pause until all checks complete.

✅ Focus: Use Event as a manual release trigger for paused threads.


"""
