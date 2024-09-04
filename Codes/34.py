def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

Factorials = {'0':0,
              '1':0,
              '2':0,
              '3':0,
              '4':0,
              '5':0,
              '6':0,
              '7':0,
              '8':0,
              '9':0}

for i in Factorials.keys():
    Factorials[i] = factorial(int(i))

Ans = 0
i = 2
ttl = 200

while ttl > 0:
    i += 1
    temp = 0
    for x in str(i):
        temp += Factorials[x]
    if temp == i:
        Ans += i
        ttl = 1000000
    else:
        ttl -= 1
print(Ans)