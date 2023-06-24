from collections import deque

n = int(input())
ans = []
cards = deque([])
cnt = n

for i in range(n):
    cards.append(i+1)
    ans.append(i+1)

skills = input().split()

for i in skills:
    if i == "1":
        ans[cards.popleft() -1] = cnt
        cnt-=1
    elif i == "2" and len(cards) >= 2:
        ans[list(cards)[1] - 1] = cnt
        cards.remove(list(cards)[1])
        cards = deque(cards)
    elif i == "3" and len(cards) >= 2:
        ans[cards.pop() -1] = cnt
        cnt-=1

  
for i in ans:
    print(ans, end=" ")