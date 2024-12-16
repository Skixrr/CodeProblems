def prime_factors(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors


def solution():
	for n in range(7000, 700000):
		if len(prime_factors(n)) >= 4 and len(prime_factors(n + 1)) >= 4 and len(prime_factors(n + 2)) >= 4 and len(prime_factors(n + 3)) >= 4:
			print(n)
			return n

solution()

