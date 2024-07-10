Primes = [2,3]
Ans = 1
for i in range(2,2000000):
    if i%2==0:
        pass
    else:
        for Prime in Primes:
            if i % Prime == 0:
                break
        else:
            Primes.append(i)

for i in Primes:
    Ans += i
print(Ans)