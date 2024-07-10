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
    for Power in range(Question,1,-1):
        if i**Power < Question:
            Ans = Ans * i**Power
            break

for i in range(1,Question):
    if Ans%i != 0:
        print(i)
        Ans = Ans * i

print(Ans)