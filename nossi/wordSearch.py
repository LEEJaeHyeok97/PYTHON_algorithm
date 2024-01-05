def exist(self, board, word):
    n, n = len(board), len(board[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = False

    def in_range(i, j):
        if i >= 0 and i < n and j >= 0 and j < m:
            return True
        return False
    
    def backtracking(i, j, w, visited):
        if not visited[i][j] and board[i][j] == word[w]:
            