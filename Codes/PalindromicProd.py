Digits = 3
Lowest = 585
Largest = int('9' * Digits)

Num1 = Largest
Num2 = Largest
product = 100

while str(product)[::-1] != str(product):
    if Num1 < Lowest:
        Num2 -= 1
        Num1 = Num2
    Num1 -= 1
    product = Num1*Num2
    print(Num1,Num2)
print(Num2*Num1)
