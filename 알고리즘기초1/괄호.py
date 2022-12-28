import sys

n = int(sys.stdin.readline())

for i in range(n):
    flag = 0
    lst = []
    bracket = list(map(str, sys.stdin.readline().strip()))
    for j in bracket:
        if j == "(":
            lst.append(j)
        elif j == ")":
            if len(lst) == 0:
                flag = 1
                print("NO")
                break
            lst.pop()
    
    if len(lst) != 0:
        print("NO")
    elif flag == 1:
        continue
    else:
        print("YES")
