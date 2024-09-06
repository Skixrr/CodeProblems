def factorialFinder(n):
    factorial = n
    for i in range(1,n):
        factorial = factorial * i
    return factorial

FactStr = str(factorialFinder(100))
Ans = 0

for i in FactStr:
    Ans += int(i)

print(Ans)