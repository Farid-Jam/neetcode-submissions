class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for r in range(9)]
        cols = [set() for c in range(9)]
        boxes = [set() for b in range(9)]

        for r in range(9):
            for c in range(9):
                cell = board[r][c]
                if cell == '.':
                    continue
                if cell in rows[r] or cell in cols[c] or cell in boxes[r // 3 * 3 + c // 3]:
                    return False
                rows[r].add(cell)
                cols[c].add(cell)
                boxes[r // 3 * 3 + c // 3].add(cell)
        return True