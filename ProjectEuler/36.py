def den2bin(n,val=''):
    if n%2 == 1:
        val = val + '1'
    else:
        val = val + '0'
    n = n // 2
    if n != 0:
        return den2bin(n,val)
    else:
        return val[::-1]
def pal10(n):
    val = 0
    num = n
    while num != 0:
        val *= 10
        val += (num%10)
        num = num//10
    if n == val:
        return True
    else: return False


ans = 0

for i in range(1,1000000,2):
    j = den2bin(i)
    if j == j[::-1]:
        if pal10(i):
            ans += i
print(ans)
