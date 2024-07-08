#1) Find prime numbers
#2) See the largest of which that go into 600851475143
# 13195 -> 5,7,13,29
n = 600851475143
Factors = []
Primes = [2,3,5,7,11,13,17,23,29]
Counter = 0


for i in range(29,int(n**0.5)):
    if i%2==0:
        pass
    else:
        print(i)
        for Prime in Primes:
            if i % Prime == 0:
                break
        else:
            Primes.append(i)
print(Primes)


while n != 1: #Finding the Prime Factors
    if n % Primes[Counter] == 0:
        Factors.append(Primes[Counter])
        n = n/Factors[-1]
    else:
        Counter += 1

print(Factors)
