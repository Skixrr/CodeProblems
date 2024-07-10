N = 10001
Primes = [2]
i = 3
while len(Primes) != N:
    for Prime in Primes:
        if i%Prime == 0:
            break
    else:
        Primes.append(i)
    print(Primes)
    i += 1