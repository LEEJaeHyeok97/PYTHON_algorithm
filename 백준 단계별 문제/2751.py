import sys

n = int(input())

l = []

for i in range(n):
    l.append(int(sys.stdin.readline()))

l2 = set(l)

l = list(l2)

l.sort()

for i in l:
    print(i)