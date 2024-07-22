#   "Создание функций на лету"
from random import choice

#   lambda:
first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(f'lambda-function: {result}')
print('_________________')


#   Замыкание:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w+') as file:
            for x in data_set:
                file.write(str(x) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        random_word = choice(self.words)
        return random_word


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(f'__call__-method: ')
print(first_ball())
print(first_ball())
print(first_ball())
