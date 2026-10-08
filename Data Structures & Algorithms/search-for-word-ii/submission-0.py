class TrieNode():
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        res = []
        curWord = []
        
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.endOfWord = True
        
        def dfs(r, c, node):
            if node.endOfWord:
                node.endOfWord = False
                res.append("".join(curWord))
            
            if not node.children:
                return
            
            for x, y in self.directions:
                nr, nc = r + x, c + y
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in node.children:
                    letter = board[nr][nc]
                    curWord.append(letter)
                    board[nr][nc] = '.'
                    dfs(nr, nc, node.children[letter])
                    curWord.pop()
                    board[nr][nc] = letter
            
        m = len(board)
        n = len(board[0])
        for r in range(m):
            for c in range(n):
                if board[r][c] in root.children:
                    letter = board[r][c]
                    curWord.append(letter)
                    board[r][c] = '.'
                    dfs(r, c, root.children[letter])
                    curWord.pop()
                    board[r][c] = letter
        
        return res