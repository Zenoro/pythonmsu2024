def sieve_of_eratosthenes(limit):
    prime_flags = [True] * (limit + 1)
    p = 2
    while (p ** 2 <= limit):
        if (prime_flags[p] == True):
            for i in range(p ** 2, limit + 1, p):
                prime_flags[i] = False
        p += 1
    primes = [p for p in range(2, limit + 1) if prime_flags[p]]
    return primes


input_data = int(input())
limits = sieve_of_eratosthenes(100)
for lim in limits:
    if round(input_data**(1/lim)) == round(input_data**(1/lim), 5):
        print("YES")
        quit(0)
print("NO")
