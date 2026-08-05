class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0
        def deleteIsland(i, j):
            grid[i][j] = "0"
            for direction in directions:
                row = i + direction[0]
                col = j + direction[1]
                if row < 0 or len(grid) <= row or col < 0 or len(grid[0]) <= col:
                    continue
                if grid[row][col] == "1":
                    deleteIsland(row, col)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    deleteIsland(i, j)
        
        return islands