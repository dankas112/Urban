def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        is_prime_bool = True
        for divider in range(2, res):
            if res == 1:
                is_prime_bool = False
            if res == divider:
                continue
            if res % divider == 0:
                is_prime_bool = False
                break
        if is_prime_bool:
            print('Простое')
        else:
            print('Составное')
        return res

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

