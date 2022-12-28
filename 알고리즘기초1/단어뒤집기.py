import sys

n = int(sys.stdin.readline())

for i in range(n):
    lst = sys.stdin.readline().split()

    for i in lst:
        i = str(i)
        print(i[::-1], end=" ")
    print()