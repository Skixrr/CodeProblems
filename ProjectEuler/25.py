memo = [1,1]
while len(str(memo[-1])) < 1000:
    memo.append(memo[-1] + memo[-2])
print(len(memo))