from collections import deque, defaultdict

# def bfs4(graph, start_v):
#     visited = [start_v]
#     queue = deque(start_v)
#
#     while queue:
#         cur_v = queue.popleft()
#         for i in graph[cur_v]:
#             if i not in visited:
#                 visited.append(i)
#                 queue.append(i)

graph = defaultdict(list)


N, M, K, X = map(int, input().split())
queue = deque()

for i in range(M):
    start_v, end_v = map(int, input().split())
    graph[start_v].append(end_v)





def bfs(graph, start_v):
    ans = []
    visited = {start_v: 0}
    queue = deque([start_v])



    while queue:
        cur_v = queue.popleft()
        cur_depth = visited[cur_v]

        if cur_depth == K:
            ans.append(cur_v)



        for i in graph[cur_v]:
            if i not in visited:
                queue.append(i)
                visited[i] = cur_depth + 1

    return ans



result_arr = bfs(graph, X)

if result_arr == []:
    print("-1")

for i in result_arr:
    print(i)