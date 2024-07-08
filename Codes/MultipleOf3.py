i = 1000
Ans = 0
while i > 0:
    i -= 1
    if i % 3 == 0 or i % 5 == 0:
        Ans += i
print(Ans)
