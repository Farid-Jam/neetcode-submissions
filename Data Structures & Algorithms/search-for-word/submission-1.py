class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = [[False] * len(board[0]) for _ in range(len(board))]
        if len(word) < 1:
            return False

        def dfs(i, j, idx):
            if idx >= len(word):
                return True
            for direction in directions:
                row = i + direction[0]
                col = j + direction[1]
                if row < 0 or len(board) <= row or col < 0 or len(board[0]) <= col or visited[row][col] == True :
                    continue
                if board[row][col] == word[idx]:
                    visited[row][col] = True
                    if dfs(row, col, idx + 1):
                        return True
                    visited[row][col] = False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(i, j, 1):
                        return True
                    visited[i][j] = False

        return False