d = []

for i in range(100):
    d.append([0] * 100)


n = int(input())

square = []

for i in range(n):
    square.append(list(map(int,(input().split()))))

#painting
for k in square:
    x = k[0]
    y = k[1]
    for i in range(10):
        for j in range(10):
            d[x + i][y + j] = 1


area = 0

#넓이 검사
for i in range(100):
    for j in range(100):
        if d[i][j] == 1:
            area+=1

print(area)