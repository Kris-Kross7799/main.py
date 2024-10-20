import time
from threading import Thread
import queue
from time import sleep
from random import randint

class Table:
    def __init__(self,number):
        self.number=number
        self.guest=None

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name=name

    def run(self):
        time.sleep(randint(3,10))  #гость ждет случайное время

class Cafe():
    def __init__(self, *tables: list):
        self.queue=queue.Queue()
        self.tables=tables

    def guest_arrival(self, *quests):
        for guest in guests:
            seated=False
            for table in self.tables:
                if table.guest is None:
                    table.guest=guest
                    print(f"{guest.name} сел(а) за стол: {table.number}")
                    guest.start() #запускаем поток гостя
                    seated=True
                    break
                else:
                    self.queue.put(guest) #помещаем гостя в очередь
                    print(f"{guest.name} в очереди")


    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest !=None for table in self.tables):
            for table in self.tables:
                if table.guest:
                    if not table.guest.is_alive():   #Гость поел
                        print(f"{table.guest.name} поел и ушёл")
                        print(f"Стол номер: {table.number} свободен")
                        table.guest=None #Освобождаем стол

                    if self.queue.qsize()>0 and table.guest is None:
                        guest_from_queue=self.queue.get()   #Берём гостя из очереди
                        table.guest=guest_from_queue        #Садим его за стол
                        print(f"{guest_from_queue} вышел из очереди и сел за стол номер {table.number}")
                        guest_from_queue.start()    #Запускаем поток нового гостя


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()