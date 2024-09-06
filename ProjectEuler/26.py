num = 1000
primes = []
d = []

def PatternLen(index,offset):
    global d
    temp = ''
    

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
 
# Add all prime numbers to array
for p in range(2, num+1):
    if prime[p]:
        primes.append(p)
        d.append(p)



for i in range(0,len(d)):
    d[i] = 1/d[i]
    d[i] = str(d[i])
    d[i] = d[i][2::]
    if (int(d[i]) * primes[i]) % 10 == 0:
        d[i] = False
    else:
        d[i] = str(d[i])[:-1]

for i in range(0,len(d)):
    if type(d[i]) != str:
        continue
    else:
        temp = ''
        for i in d[i]:
