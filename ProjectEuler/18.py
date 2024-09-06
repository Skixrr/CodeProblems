pyramid = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
line = 0
Arr = [[]]
temp = None
for i in pyramid:
    if i == ' ':
        temp = None
    elif temp == '0' and i == '0':
        Arr[line].append(0)
    elif i == '\n':
        line += 1
        Arr.append([])
        temp = None
    else:
        if temp != None:
            val = temp*10
            Arr[line].append(val+int(i))
        else:
            temp = int(i)

answer = 0
def greedyPath(x,y):
    global answer
    print(Arr[y][x])
    answer += Arr[y][x]
    if len(Arr)-1 == y:
        print(answer)
    elif len(Arr)-2 == y:
        if Arr[y+1][x] > Arr[y+1][x+1]:
            return greedyPath(x,y+1)
        else:
            return greedyPath(x+1,y+1)
    else:
        if Arr[y+1][x] + Arr[y+2][x] >= Arr[y+1][x+1] + Arr[y+2][x+1] or Arr[y+1][x] + Arr[y+2][x] >= Arr[y+1][x+1] + Arr[y+2][x+2]:
            return greedyPath(x,y+1)
        elif Arr[y+1][x] + Arr[y+2][x+1] >= Arr[y+1][x+1] + Arr[y+2][x+1] or Arr[y+1][x] + Arr[y+2][x+1] >= Arr[y+1][x+1] + Arr[y+2][x+2]:
            return greedyPath(x,y+1)
        else:
            return greedyPath(x+1,y+1)
greedyPath(0,0)