# tuple:
immutable_var = (1.44, 'It is a tuple', 55, True, False, 77)
print(immutable_var)
immutable_var.append('Not working')
immutable_var.insert(2, 100)
# Traceback (most recent call last):
#   File "C:\Users\danii\OneDrive\Рабочий стол\PY\Urban\Module1\hw5.py", line 4, in <module>
#     immutable_var.append('Not working')
#     ^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'tuple' object has no attribute 'append'


# list:
mutable_list = [1.44, 'It is a tuple', 55, True, False, 77]
print(mutable_list)
mutable_list.append('Not working')
mutable_list.insert(2, 100)
print(mutable_list)
