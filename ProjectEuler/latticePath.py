def factorialFinder(n):
    factorial = n
    for i in range(1,n):
        factorial = factorial * i
    return factorial

numerator = factorialFinder(40)
denominator = factorialFinder(20)**2
print(numerator/denominator)
