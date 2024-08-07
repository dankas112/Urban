import threading
from time import sleep
from random import randint
import queue

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.tables = tables
        self.queue = None

    def guest_arrival(self, *quests):
        pass

    def discuss_guests(self):
        pass
