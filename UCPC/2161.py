from collections import deque
queue = deque([])
ans = []

n = int(input())
for i in range(1, n+1):
    queue.append(i)


while queue:
    card = queue.popleft()
    ans.append(card)
    if queue:
        card = queue.popleft()
        queue.append(card)

for i in ans:
    print(i, end=" ")