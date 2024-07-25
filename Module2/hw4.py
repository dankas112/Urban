numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
i = 0
for number in numbers:
    for divider in numbers[1:i]:
        if number % divider == 0:
            is_prime = False
        elif not is_prime:
            not_primes.append(number)
            break
    if is_prime:
        primes.append(number)
    i += 1
    is_prime = True

primes.remove(1)
print(primes)
print(not_primes)
