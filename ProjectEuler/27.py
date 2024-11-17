num = 99999999
primes = []

#Sieve
prime = [True for i in range(num+1)] #Boolean array of length num
p = 2
while (p**2 <= num):
    # If prime[p] is not changed, then it is a prime
    if (prime[p] == True): 
        # Updating all multiples of p
        for i in range(p**2, num+1, p):
            prime[i] = False
    p += 1
 
# Print all prime numbers
for p in range(2, num+1):
    if prime[p]:
        primes.append(p)

print('Primes found')

product = 0
consecutives = 0
for a in range(-1000,1001):
    if a == 0:
        print('halfway there')
    for b in range(2,1001):
        n = 0
        if (n**2 + a*n + b) > 1:
            while (n**2 + a*n + b) in primes:
                n += 1
        if n > consecutives:
            consecutives = n
            product = a*b
print(product)
