import math
N = 2

def countTriangles():
    global N
    count = int(0.5*(3*N*N + N))
    if count%2 == 1:
        count += 1
        count // 2
    else:
        count // 2
    return count

triangles = countTriangles()

cricket = (N,0)
a = (0,0)
b = (N/2,N)
c = (3*N/2,N)
d = (2*N,0)
e = (3*N/2,-N)
f = (N/2,-N)

def move(edge):
    global cricket
    x = (cricket[0] + edge[0])/2
    y = (cricket[1] + edge[1])/2
    cricket = (x,y)
    return None

def reset():
    global cricket
    cricket = (N,0)
    return None

def NewTriangle(left=(0,0)):
    right = (left[0] + 1, left[1])
    top = (left[0]+0.5,left[1] + 1)
    return [left,right,top]

def shoelace(a,b,c):
    return 0.5 * abs((a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0]))

def check(cricket,triangle):
    left = triangle[0]
    right = triangle[1]
    top = triangle[2]
    A = shoelace(left,right,top)
    u = shoelace(cricket,right,top)/A
    v = shoelace(cricket,left,top)/A
    w = shoelace(cricket,right,left)/A
    return (u+v+w) == 1

