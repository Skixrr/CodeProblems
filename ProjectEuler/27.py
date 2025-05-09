num = 391000
primes = set()

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
        primes.add(p)
product = 0
count = 0
for b in range(-1000,1000):
    for c in range(-1000,1000):
        temp = 0
        for n in range(0,1000):
            val = (n**2 + b*n + c)
            if val < 2:
                break
            elif val in primes:
                temp += 1
            else:
                break
        if temp > count:
            product = b*c
            count = temp
        temp = 0
print(product,count)

