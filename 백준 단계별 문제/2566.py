m = []

for i in range(9):
    m.append(list(map(int, input().split())))

max = 0
index =[0, 0]

for i in range(9):
    for j in range(9):
        if m[i][j] > max:
            max = m[i][j]
            index[0] = i
            index[1] = j

        

print(max)
print(index[0] + 1, index[1] + 1)