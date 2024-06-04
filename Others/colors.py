# package termcolor isn't support windows
import termcolor
from colorama import init
init(autoreset=True)

# print(Fore.GREEN + 'blabla')

print('color')
print("\033[31mЭтот текст должен быть красным\033[0m")
print("\033[32mЭтот текст должен быть зеленым\033[0m")
print("\033[34mЭтот текст должен быть синим\033[0m")

termcolor.cprint('colors', color='green')
print(termcolor.colored('wait what', 'green'))