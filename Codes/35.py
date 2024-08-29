num = 1000000
Count = 0
Proven = []

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
 


def Circle(n):
    global Proven
    if n in Proven:
        pass
    else:
        Circular = True
        Rotations = []
        loops = len(str(n))
        string = str(n)
        global prime
        global Count

        while loops >= 1:
            if not prime[int(string)]:
                Circular = False
            else:
                Rotations.append(int(string))
                string = string[-1] + string
                string = string[:-1]
            loops -= 1
        if Circular == True:
            print(n)
            for i in Rotations:
                Count += 1
                Proven.append(i)

# Print all prime numbers
for p in range(2, num+1):
    if prime[p]:
        Circle(p)

print(sorted(Proven))