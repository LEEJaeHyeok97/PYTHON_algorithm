a, b, c, d, e, f = map(int, input().split())
ans = []

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if a*i + b*j == c and d*i + e*j == f:
            ans.append(i)
            ans.append(j)
for i in ans:
    print(i, end = " ")