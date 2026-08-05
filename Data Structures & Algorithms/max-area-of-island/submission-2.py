class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        maxArea = 0
        rows, cols = len(grid), len(grid[0])

        def deleteIsland(r, c):
            grid[r][c] = 0
            area = 1
            for direction in directions:
                row = r + direction[0]
                col = c + direction[1]
                if row < 0 or len(grid) <= row or col < 0 or len(grid[0]) <= col:
                    continue
                elif grid[row][col] == 1:
                    area += deleteIsland(row, col)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, deleteIsland(r, c))

        return maxArea