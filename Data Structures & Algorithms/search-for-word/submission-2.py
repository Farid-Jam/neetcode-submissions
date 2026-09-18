class Solution:
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or r >= m or c < 0 or c >= n:
                return False

            if board[r][c] != word[i]:
                return False
            
            letter = board[r][c]
            board[r][c] = '.'
            
            for d in self.directions:
                found = dfs(r + d[0], c + d[1], i + 1)
                if found:
                    return True
            
            board[r][c] = letter
            return False
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    found = dfs(r, c, 0)
                    if found:
                        return True

        return False
