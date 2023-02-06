from collections import deque

people = deque()

n, k = map(int, input().split())

for i in range(1, n+1):
    people.append(i)

answer = []

while people:
    for i in range(k-1):
        people.append(people.popleft())
    answer.append(people.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))