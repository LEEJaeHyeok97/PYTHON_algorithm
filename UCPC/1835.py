from collections import deque

n = int(input())
ans = [0]*n
cards = deque([])
cnt = 1

for i in range(1, n+1):
    cards.append(i)

while cards:
    for i in range(cnt):
        cards.append(cards.popleft())
    ans[cards.popleft()-1] = cnt
    cnt+=1 

for i in ans:
    print(i, end=" ")