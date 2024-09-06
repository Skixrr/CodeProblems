def d(n):
    return sum(x for x in range(1, n // 2 + 1) if not (n % x))


s = set()
for i in range(1, 10000):
    m = d(i)
    n = d(m)
    if (i == n) and (m != n):
        s.add(m)

print(sum(s))