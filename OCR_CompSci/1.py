def recurFactorial(n):
    if n == 0 or n == 1:
        return 1
    else: return n * recurFactorial(n-1)

def loopFactorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fact = n
        while n > 1:
            n -= 1
            fact *= n
        return fact

print(recurFactorial(5))
print(loopFactorial(5))
    