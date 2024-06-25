hw1 = 'hw1\\hw1.txt'
with open(hw1, mode='r', encoding="utf8") as file:
    for line in file:
        print(line, end='')

