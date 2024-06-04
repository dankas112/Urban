from nim_engine import get_bunches, put_stones, take_from_bunch, is_gameover
from termcolor import cprint, colored
from colorama import init

init(autoreset=True)

put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', 'green')
    cprint(get_bunches(), 'green')
    user_color = 'blue' if user_number == 1 else 'yellow'
    cprint('Ход игрока {}'.format(user_number), user_color)
    pos = input(colored('Откуда берем?', user_color))
    qua = input(colored('Сколько берем?', user_color))
    step_successed = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_successed:
        user_number = 2 if user_number == 1 else 1
    else:
        cprint('Невозможный ход!', 'red')
    # take_from_bunch(position=int(pos), quantity=int(qua))
    if is_gameover():
        break

cprint('Выиграл игрок номер {}'.format(user_number), 'red')
