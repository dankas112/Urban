from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали')
        enemies = 100
        battle_days = 0
        while enemies != 0:
            enemies -= self.power
            battle_days += 1
            print(f'{self.name} сражается {battle_days} день\дня\дней..., осталось {enemies} воинов\n')
            sleep(1)
        else:
            print(f'{self.name} одержал победу спустя {battle_days} день\дня\дней')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
