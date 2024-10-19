falses = [1]
trues = [89]
def chain(n):
    global falses
    global trues
    n = str(n)
    temp = 0
    for i in n:
        temp += (int(i)**2)
    if temp in trues:
        return True
    elif temp in falses:
        return False
    else:
        return chain(temp)
count = 0
for j in range(1,10000000):
    if chain(j):
        trues.append(j)
        count += 1
    else:
        falses.append(j)
print(count)