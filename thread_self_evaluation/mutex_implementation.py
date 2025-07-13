"""
You are simulating a shared bank account accessed by multiple ATM machines (threads).
Each ATM thread tries to withdraw money 10 times.
The initial balance is 100. If the balance is not enough for a withdrawal,
the ATM should print "Insufficient balance".
Use a Lock to ensure that two threads never check or update the balance at the same time.

"""
import threading
from threading import Lock

lock=threading.Lock()



class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        """
        :param amount:
        :return:

        lock.acquire()
        try:
            if something:
                return result  # ❌ danger: might skip lock.release()
        finally:
            lock.release()

                                    Return only works securely with "with lock" and not with lock.acquire()
                                    The lock is released automatically (with lock: handles it)
                                    No cleanup is skipped
                                    The return value is used if needed

        """
        try:
            with lock:
                if self.balance>=amount:
                    self.balance-=amount
                    print(f"[{threading.current_thread().name}] Withdrawn {amount}, Current balance: {self.balance}")
                    return "current balance = " +str(self.balance)
                else:
                    print(f"[{threading.current_thread().name}] Insufficient balance")
                    return "Insufficient balance"
        except ValueError:
            print("Insufficient balance or incorrect amount")

    def current_balance(self):
        with lock:
            print(f"[{threading.current_thread().name}] Balance check: {self.balance}")
            return self.balance

if __name__=="__main__":
    bank=BankAccount(100)
    threads=[]
    for i in range(10):
        atm1=threading.Thread(target=bank.withdraw, args=(10,),name=f"ATM1-W-{i}")
        atm2=threading.Thread(target=bank.current_balance,args=(),name=f"ATM2-R-{i}")
        threads.extend([atm1,atm2])
        atm1.start()
        atm2.start()

    for thread in threads:
        thread.join()

    print("Final balance:", bank.current_balance())
