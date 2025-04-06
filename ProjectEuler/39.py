squares = []
for i in range(1000):
    squares.append(i**2)
p = {}
i = 1
while i != 500:
    j = i
    while j != 500:
        if (squares[i] + squares[j]) in squares:
            k = squares.index(squares[i] + squares[j])
            if str(i+j+k) not in p.keys():
                p[str(i+j+k)] = 1
            else:
                p[str(i+j+k)] += 1
        j += 1
    i += 1
mx = 0
mp = 0
for i in p.keys():
    if p[i] >= mx:
        mx = p[i]
        mp = i
print(mp)