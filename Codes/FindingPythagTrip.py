Question = 1000
a = 3
b = 4
c = 5
while a + b + c != Question:
    if a == b:
        a = 1
        b += 1
    else:
        a += 1
    c = (a**2 + b**2)**0.5

print(a*b*c)