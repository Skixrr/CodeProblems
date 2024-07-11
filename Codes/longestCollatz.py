def Collatz(Start):
    Sequence = [Start]
    while Sequence[-1] != 1:
        if Sequence[-1]%2 == 0:
            Sequence.append(Sequence[-1]//2)
        else:
            Sequence.append((3*Sequence[-1])+1)
    return Sequence
Ans = 0
for i in range(1,1000000):
    temp = len(Collatz(i))
    if temp > Ans:
        Ans = temp
print(Ans)