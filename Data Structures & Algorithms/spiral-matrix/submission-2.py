class Solution:
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        borders = [0, n, m, 0]

        d = 0
        res = []
        r, c = 0, 0
        for i in range(m * n):
            res.append(matrix[r][c])

            nr, nc = r + self.directions[d][0], c + self.directions[d][1]
            if nr < borders[0] or nr >= borders[2] or nc < borders[3] or nc >= borders[1]:
                if d == 0 or d == 3:
                    borders[d] += 1
                else:
                    borders[d] -= 1
                
                d += 1
                d %= 4

                nr, nc = r + self.directions[d][0], c + self.directions[d][1]
            r, c = nr, nc
        return res