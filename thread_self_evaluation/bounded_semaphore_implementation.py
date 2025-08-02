"""
BoundedSemaphore (threading.BoundedSemaphore)
🔸 Problem Statement: Ticket Booking System
Simulate a ticket booking system with 5 total tickets. Users (threads) try to book one ticket each. Prevent overbooking using a BoundedSemaphore(5).
If a user thread tries to book when no tickets are available, show a message saying "Sold Out".

✅ Focus: Prevents accidental over-release (can’t release more than acquired).

"""
import asyncio

"""

"""
class TicketBookingSystem:
    def __init__(self,totalTickets):
        self.tickets=totalTickets

    async def book(self,ticket):
        await ticket.acquire()


if __name__== "__main__":
    threads=[]
    ticketSystem=TicketBookingSystem()
    for i in range(5):
        ticketThread=asyncio.BoundedSemaphore(target=ticketSystem.book, value=20)
        threads.append(ticketThread)
    await asyncio.wait(threads)

    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())
    print("LOOP COMPLETED")
    loop.close()
