def Sieve(num):
    primes = []
    #
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
    #
    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            primes.append(p)
    return primes
primes = Sieve(1000)

def division(N):
    print(N)
    count = 0
    M = 1
    if N > 100:
        M *= 1000
    elif N > 10:
        M *= 100
    else:
        M *= 10
    M = M%N
    while M != 1 and M!=0:
        if N > 100:
            M *= 1000
        elif N > 10:
            M *= 100
        else:
            M *= 10
        M = M%N
        count += 1
    return count

mx = [0,0]
for i in primes:
    C = division(i)
    if mx[1] < C:
        mx = [i,C]
print(mx)