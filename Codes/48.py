Ans = 0
i = 1

while i != 1001:
    temp = (i**i) % (10**10)
    Ans += temp
    Ans = Ans % (10**10)
    i += 1

print(Ans)