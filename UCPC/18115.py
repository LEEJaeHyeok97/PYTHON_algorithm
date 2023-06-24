from collections import deque

n = int(input())
li = list(map(int, input().split()))
li.reverse()

cards = deque()

for i in range(n):
    if li[i] == 1:
        cards.appendleft(i+1)
    elif li[i] == 2:
        cards.insert(1, i+1)
    elif li[i] == 3:
        cards.append(i+1)

for card in cards:
    print(card, end=" ")