import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, mode='r', encoding='utf8') as file:
        reading = file.readlines()
        all_data.append(reading)
    return None


files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

if __name__ == '__main__':
    start1 = datetime.now()
    for x in files:
        read_info(x)
    end1 = datetime.now()
    print('Линейный вызов: ', end1 - start1)

    start = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    end = datetime.now()
    print('Многопроцессный: ', end - start)
