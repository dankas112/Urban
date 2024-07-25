first = input('Введите 1е число: ')
second = input('Введите 2е число: ')
third = input('Введите 3е число: ')
numbers = [first, second, third]
numbers = set(numbers)
if len(numbers) == 1:
    print(3)
elif len(numbers) == 2:
    print(2)
else:
    print(0)
