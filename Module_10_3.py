import threading
from threading import Lock
import time
from random import randint

class Bank:
    def __init__(self):
        self.balance=0
        self.lock=Lock()

    def Deposit(self):
        for i in range(100):
            a=randint(50,500)
            with self.lock:
                self.balance+=a
                print(f"Пополнение: {a}, текущий баланс: {self.balance}")
            if self.balance>=500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def Take(self):
        for i in range(100):
            b=randint(50,500)
            with self.lock:
                print(f"Запрос на {b}")
                if b<=self.balance:
                    self.balance-=b
                    print(f"Снятие: {b}. Баланс: {self.balance}")
                else:
                    print(f"Запрос отклонён, недостаточно средств")
            time.sleep(0.001)
        self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.Deposit, args=(bk,))
th2 = threading.Thread(target=Bank.Take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')


