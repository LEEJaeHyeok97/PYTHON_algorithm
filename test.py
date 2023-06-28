import sys
N, M = map(int, input().split())

graph = []
for i in range(M):
    tmp = input()
    arr = []
    for j in str(tmp):
        arr.append(int(j))
    graph.append(arr)

visited = []
for _ in range(M):
    visited.append([0]*N)

print(visited)

def dfs(cur_x, cur_y):
    visited[cur_x][cur_y] = 1
    for v in graph[cur_x][cur_y]:
        if v not in visited:
            dfs(cu)