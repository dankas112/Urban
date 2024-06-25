team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'


# %:
# team1_num = 7
print(f'{'%':_^10}')
print("В команде Мастера кода участников: %d ! " % team1_num)
print('Итого сегодня в командах участников: %d и %d !' % (team1_num, team2_num))


# .format:
print(f'{'.format':_^10}')
print("Команда Волшебники данных решила задач: {} !".format(score2))

print("Волшебники данных решили задачи за {} с !".format(team1_time))

# f''
print(f'{'new':_^10}')
print(f"Команды решили {score1} и {score2} задач.")

print(f'Результат битвы: {challenge_result}!')

print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')



