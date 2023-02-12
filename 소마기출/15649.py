# #DFS
# N, M = map(int, input().split())

# arr = [i for i in range(1, N+1)]
# check = [False] * len(arr)

# a= []

# def DFS(v):
#     if v == M:
#         print(*a, sep=' ')
#         return
        
#     for i in range(N):
#         if check[i]:
#             continue
#         check[i]=True
#         a.append(arr[i])
#         DFS(v+1)
#         a.pop()
#         check[i] = False
    
        

# DFS(0)