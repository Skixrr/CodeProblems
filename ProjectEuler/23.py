import math
def getDivisors(num):
    if num==1:
        return 1
    n = math.ceil(math.sqrt(num))
    total = 1
    divisor = 2
    while (divisor < n):
        if (num%divisor == 0):
            total += divisor
            total += num//divisor
        divisor+=1
    if n**2==num:
        total+=n
    return total
def isAbundant(num):
    if (getDivisors(num) > num):
        return True
    else:
        return False

abundentNums = []
for x in range (0,28124):
    if (isAbundant(x)):
        abundentNums.append(x)
del abundentNums[0]

sums = [0]*28124
for x in range (0, len(abundentNums)):
    for y in range (x, len(abundentNums)):
            sumOf2AbundantNums = abundentNums[x]+abundentNums[y]
            if (sumOf2AbundantNums<= 28123):
                if (sums[sumOf2AbundantNums] == 0):
                    sums[sumOf2AbundantNums] = sumOf2AbundantNums

total = 0
for x in range (1,len(sums)):
    if (sums[x] == 0):
        total +=x
print(total)