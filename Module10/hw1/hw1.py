from time import sleep
from threading import Thread
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, mode='w', encoding='utf8') as file:
        for word in range(1, word_count + 1):
            file.write(f'Какое-то слово №{word}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


# _______________________FUNCTIONS_____________________________

time_F_start = datetime.now()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_F_end = datetime.now()
print('Работа функций:', time_F_end - time_F_start)

# _______________________THREADS______________________________
example_5 = (10, "example5.txt")
example_6 = (30, "example6.txt")
example_7 = (200, "example7.txt")
example_8 = (100, "example8.txt")

time_T_start = datetime.now()

e1 = Thread(target=write_words, args=example_5)
e2 = Thread(target=write_words, args=example_6)
e3 = Thread(target=write_words, args=example_7)
e4 = Thread(target=write_words, args=example_8)

e1.start()
e2.start()
e3.start()
e4.start()

e1.join()
e2.join()
e3.join()
e4.join()

time_T_end = datetime.now()
print('Работа потоков:', time_T_end - time_T_start)
