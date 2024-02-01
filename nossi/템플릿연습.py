# def solution(nums, target):
#
#     grid = [
#
#     ]
#
#     return False
#
# print(solution())

from collections import deque

from collections import deque


# class Solution:
#     def numIslands(self, grid):
#         cnt = 0
#         row_len = len(grid)
#         col_len = len(grid[0])
#
#         visited = [[False] * col_len for i in range(row_len)]
#
#         def dfs(r, c):
#             dr = [-1, 1, 0, 0]
#             dc = [0, 0, 1, -1]
#             visited[r][c] = True
#             for i in range(4):
#                 next_r = r + dr[i]
#                 next_c = c + dc[i]
#                 if 0 <= next_r < row_len and 0 <= next_c < col_len:
#                     if grid[next_r][next_c] == "1":
#                         if visited[next_r][next_c]:
#                             dfs(next_r, next_c)
#
#         for i in range(row_len):
#             for j in range(col_len):
#                 if grid[i][j] == "1" and not visited[i][j]:
#                     dfs(i, j)
#                     cnt += 1
#         return cnt

# from collections import defaultdict
# import heapq
# class Solution:
#     def networkDelayTime(self, times: list[list[int]], n:int, k:int) -> int:
#         #단방향 그래프 만들기
#         graph = defaultdict(list)
#         for u, v, w in times:
#             graph[u].append((w, v))
#
#
#         # 다익스트라
#         costs = {}
#         heap = []
#         heapq.heappush(heap, (0, k))
#
#         while heap:
#             cur_cost, cur_v = heapq.heappop(heap)
#             if cur_v not in costs:
#                 costs[cur_v] = cur_cost
#                 for cost, next_v in graph[cur_v]:
#                     next_cost = cur_cost + cost
#                     heapq.heappush(heap, (next_cost, next_v))
#
#


# Trapping rain water
# 스택
from collections import deque

# class Solution:
#     def trap(self, height):
#         stack = []
#         ans = 0
#         for i in range(len(height)):
#             if stack and stack[-1] <= height[i]:
#                 ans += (i - stack[-1] - 1) * (height[i][1] - stack[-1])
#             stack.append((i, height[i]))
#
#
#

from collections import deque

def bfs(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

graph = {
    'A': ['B', 'D', 'E'],
    'B' : ['A', 'C', 'D'],
    'C': ['B'],
    'D': ['A', 'B'],
    'E': ['A']
}
# print(bfs(graph, 'A'))



def bfs2(graph, start_v):
    queue = deque([start_v])
    visited = [start_v]
    while queue:
        cur_v = queue.popleft()
        for i in graph[cur_v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited


print(bfs2(graph, 'A'))




def bfs3(graph, start_v):
    visited = [start_v]
    queue = deque(start_v)

    while queue:
        cur_v = queue.popleft()
        for i in graph[cur_v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

    return visited



def dfs(graph, cur_v, visited=[]):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            # visited.append(v)
            visited = dfs(graph, v, visited)

    return visited

print(dfs(graph, 'A'))

def dfs(graph, cur_v, visited=[]):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            visited = dfs(graph, v, visited)
    return visited

def dfs3(graph, cur_v, visited=[]):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            visited = dfs3(graph, v, visited)
    return visited

def bfs5(graph, start_v):
    queue = deque(start_v)
    visited = [start_v]
    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    print(visited)

















#bfs
def bfs4(graph, start_v):
    queue = deque(start_v)
    visited = [start_v]

    while queue:
        cur_v = queue.popleft()
        for i in graph[cur_v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited





print("a", bfs4(graph, 'A'))





def solution(numbers, target):
    queue = deque([(0, 0)])
    count = 0

    while queue:
        cur_idx, cur_sum = queue.popleft()
        if cur_idx == len(numbers):
            if cur_sum == target:
                count+=1
        else:
            number = numbers[cur_idx]
            queue.append((cur_idx + 1, cur_sum +number))
            queue.append((cur_idx + 1, cur_sum -number))
    return count











def dfs6(graph, cur_v, visited=[]):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            visited = dfs(graph, v, visited)
    return visited




def bfs8(graph, start_v):
    queue = deque(start_v)
    visited = [start_v]

    while queue:
        cur_v = queue.popleft()
        for v in graph[cur_v]:
            if v not in visited:
                visited.append(v)
                queue.append(v)
    return visited

print(bfs8(graph, 'A'))


def dfs6(graph, cur_v, visited=[]):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            visited = dfs6(graph, v, visited)
    return visited
print(dfs6(graph, 'A'))


















