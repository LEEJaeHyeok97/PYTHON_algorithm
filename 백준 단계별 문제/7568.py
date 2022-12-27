#count를 비교 대상보다 내가 작을 경우 +1
import sys

n = int(sys.stdin.readline())

lst = []
order = []

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    lst.append(tmp)


for i in lst:
    count = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            count+=1
    order.append(count)

for i in order:
    print(i, end=" ")