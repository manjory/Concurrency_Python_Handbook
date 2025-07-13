"""
BoundedSemaphore (threading.BoundedSemaphore)
🔸 Problem Statement: Ticket Booking System
Simulate a ticket booking system with 5 total tickets. Users (threads) try to book one ticket each. Prevent overbooking using a BoundedSemaphore(5). If a user thread tries to book when no tickets are available, show a message saying "Sold Out".

✅ Focus: Prevents accidental over-release (can’t release more than acquired).
"""
