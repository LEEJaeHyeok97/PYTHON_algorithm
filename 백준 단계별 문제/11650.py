import sys

n = int(sys.stdin.readline())

location = []

for i in range(n):
    location.append(list(map(int,(sys.stdin.readline().split()))))

location.sort()

for i in location:
    print(i[0], i[1])


