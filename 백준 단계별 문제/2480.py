count = [0, 0, 0, 0, 0, 0, 0]

dice = list(map(int, input().split(' ')))

for j in dice:
    for i in range(1, 7):
        if(j == i):
            count[i] += 1

for i in range(7):
    if(count[i] == 3):
        ans = 10000 + (i * 1000)
        break
    elif(count[i] == 2):
        ans = 1000 + (i * 100)
        break
    else:
        if(count[i] == 1):
            max = i
            ans = i * 100


print(ans)
