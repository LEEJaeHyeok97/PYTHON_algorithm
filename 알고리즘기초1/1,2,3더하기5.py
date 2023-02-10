n = int(input())

for i in range(n):
    m = int(input())
    d = [0] * (m+1)
    d[1] = 1
    d[2] = 1
    d[3] = 3

    for j in range(4, m + 1):
        d[j] = max(d[j-3] + 1, d[j-2] + 1, d[j-1] + 1)

    
    print(d[m])


