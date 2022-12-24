import sys
n = int(sys.stdin.readline())

lst = []

for i in range(n):
    age, name = (map(str, (sys.stdin.readline().split())))
    age = int(age)
    lst.append([age, name])

lst.sort(key=lambda x: (x[0]))

for i in range(n):
    print(lst[i][0], lst[i][1])

#파이썬은 기본적으로 stable 정렬을 한다