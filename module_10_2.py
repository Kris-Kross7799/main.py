from threading import Thread
import time


class Knight(Thread):
    num_of_enemies = 100
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.days=0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.num_of_enemies>0:
            # current=self.num_of_enemies
            self.num_of_enemies-=self.power
            self.days+=1
            time.sleep(1)
            print('\n'+f'{self.name} сражается {self.days} дней, осталось {self.num_of_enemies} воинов')
        print('\n'+f"{self.name} одержал победу спустя {self.days} дня(ей)!")


thread_1 = Knight('Sir Lancelot', 10)
thread_2 = Knight('Sir Galahad', 20)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
print("\nВсе битвы окончены!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)





# threads = []
# for j in range(1):
#     thread = Knight('Sir Galahad', 20)
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
