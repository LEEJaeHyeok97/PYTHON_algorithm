total = int(input())
n = int(input())

receipt = []
sum = 0

for i in range(n):
    product = list(map(int,input().split(' ')))
    receipt.append(product)
    print(product)

for i in range(n):
    sum += receipt[i][0] * receipt[i][1]

if(sum == total):
    print('Yes')
else:
    print('No')
