Count = 0
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Combinatorics = N!/(R!*(n-r)!)
def Combinatoric(n,r):
    N = factorial(n)
    R = factorial(r)
    denominator = R * factorial(n-r)
    return N // denominator

for i in range(0,101):
    for j in range(0,i):
        print([i,j])
        if Combinatoric(i,j) > 1000000:
            Count += 1

print(Count)