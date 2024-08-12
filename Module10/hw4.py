import threading as thr
from time import sleep
from random import randint
import queue


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(thr.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 4))


class Cafe:
    def __init__(self, *input_tables):
        self.tables = input_tables
        self.queue_guests = queue.Queue()

    def guest_arrival(self, *input_guests):
        for guest in input_guests:
            is_sitting = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    table.guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    is_sitting = True
                    break
            if not is_sitting:
                print(f'{guest.name} в очереди')
                self.queue_guests.put(guest)
                continue

    def discuss_guests(self):
        _is_all_tables_empty = len(self.tables)
        while not self.queue_guests.empty() and _is_all_tables_empty != 0:
            for table in self.tables:
                if table.guest and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)\n Стол номер {table.number} свободен')
                    table.guest = None
                    _is_all_tables_empty -= 1
                if not self.queue_guests.empty() and table.guest is None:
                    table.guest = self.queue_guests.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
                    _is_all_tables_empty += 1


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()
