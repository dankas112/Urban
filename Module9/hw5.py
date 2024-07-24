class StepValueError(Exception):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("Шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if self.start < self.stop:
            if self.pointer > self.stop:
                raise StopIteration()
            elif self.step < 0:     # <--start..stop(infinity loop)
                raise StopIteration
        if self.start > self.stop:
            if self.pointer < self.stop:
                raise StopIteration()
            elif self.step > 0:     # stop..start-->(some infinity loop)
                raise StopIteration
        value = self.pointer
        self.pointer += self.step
        return value


print('1:')
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)
iter6 = Iterator(1, -10)

print('2:')
for i in iter2:
    print(i, end=' ')
print()
print('3:')
for i in iter3:
    print(i, end=' ')
print()
print('4:')
for i in iter4:
    print(i, end=' ')
print()
print('5:')
for i in iter5:
    print(i, end=' ')
print()
print('6:')
for i in iter6:
    print(i, end=' ')

print('Сравнение тех же параметров введеных в range:')
print('1:')
print('Выдает ошибку: ValueError: range() arg 3 must not be zero')
# for i in range(100, 200, 0):
#     print(i, end=' ')
print('2:')
for i in range(-5, 1):
    print(i, end=' ')
print()
print('3:')
for i in range(6, 15, 2):
    print(i, end=' ')
print()
print('4:')
for i in range(5, 1, -1):
    print(i, end=' ')
print()
print('5:')
for i in range(10, 1):
    print(i, end=' ')
print()
print('6:')
for i in range(1, -10):
    print(i, end=' ')
