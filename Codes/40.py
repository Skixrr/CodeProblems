champernowne = ''
i = 1

while len(champernowne) < 1000000:
    champernowne = champernowne + str(i)
    i += 1

Ans = 1
for j in range(0,7):
    Ans = Ans * int(champernowne[(10**j)-1])
    print([10**j, champernowne[(10**j)-1], Ans])

print(Ans)