def dfs(r, c):
    visited[r][c] = True
    for i in range(4):
        next_r = r + dr[i]
        next_c = c + dc[i]
        if isValid(next_r, next_c):
            if not visited[next_r][next_c]:
                dfs(next_r, next_c)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]