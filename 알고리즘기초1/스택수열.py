import sys

n = int(sys.stdin.readline())

stack = []
ans = []
cur = 1
flag = 0

for i in range(n):
    num = int(sys.stdin.readline())
    while cur <= num:
        stack.append(cur)
        ans.append("+")
        cur+=1
    
    if(stack[-1] == num):
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in ans:
        print(i)
