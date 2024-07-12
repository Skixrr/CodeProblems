n = 1
factors = []
def findTriangle(num):
    a = 0
    for i in range(num+1):
        a += i
    return a

while len(factors) < 500:
    factors = []
    n += 1
    triangle = findTriangle(n)
    for i in range(1,int(triangle**0.5)):
        if triangle%i == 0:
            factors.append(i)
            factors.append(triangle//i)
    print(triangle)