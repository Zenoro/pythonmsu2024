def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def nonprime(n=0):
    current = n + 1
    while True:
        if current == 1 or not is_prime(current):
            yield current
        current += 1
