import sys


def introspection_info(obj):
    info = {}
    str_type = str(type(obj))
    info['type'] = str_type[8:-2]
    try:
        info['attributes'] = vars(obj)
    except:
        info['attributes'] = []

    info['methods'] = dir(obj)
    info['object module'] = sys.path[0][-8:]
    if info['type'] == 'str':
      info['symbols count'] = len(obj)
    elif info['type'] == 'int':
        info['even?'] = obj % 2 == 0
    return info


class Num:
    n = 5
    j = 4


def aboba():
    c = 12
    print(c + 12)
    return c


print(introspection_info(aboba))
print(introspection_info(Num))

number_info = introspection_info(42)
print(number_info)
