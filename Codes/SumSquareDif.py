Sum = 0
Square = 0
for i in range(1,101):
    Square += i**2
for i in range(1,101):
    Sum += i
Sum *= Sum
print(Sum-Square)