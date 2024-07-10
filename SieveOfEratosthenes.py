num = 100
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

print(primes)