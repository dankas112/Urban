data = 19
pairs_list = []
result = ''
numbers = range(1, 20)
for num in numbers:
    for num_2 in numbers:
        if num != num_2:
            if data % (num + num_2) == 0:
                if not (num, num_2) in pairs_list and not (num_2, num) in pairs_list:
                    pairs_list.append((num, num_2))
for pair in pairs_list:
    result += str(pair[0])
    result += str(pair[1])

print(result)
wtf = '118217316415514613712811910'  # (19)
if wtf == result:
    print('omg')
