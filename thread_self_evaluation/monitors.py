"""
Problem Statement: Bank Account with Monitored Deposits and Withdrawals
You are implementing a simple BankAccount class that supports concurrent deposits and withdrawals from multiple threads.

You must ensure that:

No two threads modify the balance at the same time.

Withdrawals only happen if sufficient balance exists.

You must use a threading.Lock() (monitor) to protect access to the shared balance.

💡 Requirements:
Implement a BankAccount class with:

deposit(amount)

withdraw(amount)

get_balance()

Create at least 4 threads:

Two threads deposit money ($50 each).

Two threads withdraw money ($30 and $80 respectively).

Start all threads and wait for them to finish.

Use a Lock to monitor access to the shared balance so that updates are thread-safe.

Print the final balance after all operations.

🧠 Key Concepts Practiced:
Thread-safe access to shared resources

Monitor (via Lock)

Race condition avoidance

Using threading.Thread with shared class instance
| Concept     | What it is                                                                                                  | Python Example                                        |
| ----------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **Mutex**   | A low-level lock allowing exclusive access to a critical section.                                           | `threading.Lock()`                                    |
| **Monitor** | A higher-level construct: an object whose methods are all thread-safe and coordinated via internal locking. | A class that wraps shared data + Lock inside methods. |

✅ For Monitor Practice — Here's the Adjusted Problem:
🔐 Monitor-Style Bank Account

Define a BankAccount class:

balance is private

Only accessible through:

deposit(self, amount)

withdraw(self, amount)

get_balance(self)

All methods should:

Acquire a shared Lock internally (not outside the class)

Safely update/check balance

Then write multiple threads using an instance of BankAccount.
"""
import threading

from thread_self_evaluation.mutex_implementation import lock


class BankAccount:
    def __init__(self,balance):
        self.balance=balance
        self._lock=threading.Lock()

    def deposit(self,amount):
        try:
            with self._lock:
                self.balance+=amount
                return self.balance

        except ValueError:
            print("no amount value found")

    def withdraw(self,amount):
        try:
            with self._lock:
                if self.balance>=amount:
                    self.balance-=amount
                    return "current balance= " + str(self.balance)
        except ValueError:
            print("current balance is not sufficient to withdraw amount= ",amount)

    def getBalance(self):
        with self._lock:
            return self.balance


if __name__=="__main__":
    bank=BankAccount(100)
    threads=[]
    # for item in range(4):
    thread1=threading.Thread(target=bank.deposit , args=(50,),name="deposit 1")
    thread2=threading.Thread(target=bank.deposit , args=(50,),name="deposit 2")
    thread3=threading.Thread(target=bank.withdraw , args=(30,),name="withdraw 1")
    thread4=threading.Thread(target=bank.withdraw , args=(80,),name="withdraw 2")

    threads.extend([thread1,thread2,thread3,thread4])
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


    for thread in threads:
        thread.join()

    print(f"Final Balance: {bank.getBalance()}")






