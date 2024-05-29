# Dict:
my_dict = {'Alice': 2015, 'Vanya': 2010, 'Maxim': 1998}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict.get('Vanya')}')
print(f'Not existing value: {my_dict.get('Tom')}')
my_dict.update({'Judy': 2018, "Kira": 2007})
print(f'Deleted value: {my_dict.pop('Alice')}')
print(f'Modified dictionary: {my_dict}')

print('______________')

# Set:
my_set = {0, 1, 'Good day', 5, 43.5, True, False, 1, 'oh, no', 55, 1, 43, False, 15, 'Good day'}
print(f'Set: {my_set}')
my_set.add(('Nope', True, 15.6))
my_set.update('ABC')
my_set.remove(1)
print(f'Modified set: {my_set}')
