def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print(print_params())  # default
print(print_params(1123, 44.5, 'jija'))
print(print_params(False, 5, 1))

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [42, True, 'check']
value_dict = {'a': 'gnom', 'b': 1, 'c': False}

print_params(*values_list)
print_params(**value_dict)

values_list_2 = ['pipo', 53]
print_params(*values_list_2, 42)
