class Solution:
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def deleteIsland(r, c):
            grid[r][c] = '0'

            for d in self.directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                    deleteIsland(nr, nc)
        
        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    res += 1
                    deleteIsland(r, c)
        
        return res