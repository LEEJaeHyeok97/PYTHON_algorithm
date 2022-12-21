import sys

n = int(sys.stdin.readline())

l = [0]*10001


for i in range(n):
    num = int(sys.stdin.readline())
    l[num] +=1

for i in range(len(l)):
    if l[i] != 0:
        for j in range(l[i]):
            print(i)
