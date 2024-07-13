my_seq_final = []
for i in range(1000000, 0, -1):
    ans = i
    my_seq = [ans]
    while ans != 1:
        n = ans
        if n % 2 == 0:
            ans = n/2
        else:
            ans = 3*n + 1
        my_seq.append(ans)
    my_seq_final.append(my_seq)

tmp = 0
result = [0]
for j in my_seq_final[::-1]:
    if tmp < len(j):
        tmp = len(j)
        result[0] = j
    else:
        pass
print(result[0][0])