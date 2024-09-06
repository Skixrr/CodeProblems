triangles = []
pentagons = []
hexagons = []
overlaps = 0
i = 1

def Triangular(n):
    return n * (n+1) // 2
def Pentagonal(n):
    return n * (3*n - 1) // 2
def Hexagonal(n):
    return n * (2*n -1)

while overlaps <= 2:
    i += 1
    j = Triangular(i)
    if j in pentagons and j in hexagons:
        overlaps += 1
        print(j)
    triangles.append(j)
    pentagons.append(Pentagonal(i))
    hexagons.append(Hexagonal(i))
