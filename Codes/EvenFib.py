Ans = 10
Fib = [3,5,8]
pos = 0
i = 0
while i < 4000000:
    Fib[pos] = Fib[pos-1] + Fib[pos-2]
    i = Fib[pos]
    if pos != 2:
        pos += 1
    else:
        Ans += Fib[2]
        pos = 0
print(Ans)
