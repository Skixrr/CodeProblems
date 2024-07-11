power = 2**1000
Ans = 0

while power != 0:
    temp = power%10
    Ans += temp
    power -= temp
    power = power//10
    print(power,Ans)