Primes = [2]
Question = 20
for i in range(2,Question):
    if i%2==0:
        pass
    else:
        for Prime in Primes:
            if i % Prime == 0:
                break
        else:
            Primes.append(i)
Ans = 1
print(Primes)
for i in Primes:
    Ans = Ans * i
print(Ans)