from sys import stdin
from collections import deque

# input = stdin.readline
n = int(input())
computer = {}
for i in range(n):
    computer[i+1] = set()

for j in range(int(input())):
    a, b = map(int, input().split())
    computer[a].add(b)
    computer[b].add(a)

def bfs(computer, start_v):
    visited = [start_v]
    queue = [start_v]
    while queue:
        cur_v = queue.pop()
        for v in computer[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

# def bfs(computer, start):
#     q = [start]
#     while q:
#         for i in computer[q.pop()]:
#             if i not in visited:
#                 visited.append(i)
#                 q.append(i)

print(len(bfs(computer, 1))-1)


