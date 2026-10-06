class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        firstColZero = False
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True

        firstRowZero = False
        for i in range(n):
            if matrix[0][i] == 0:
                firstRowZero = True
        
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        for i in range(1, m):
            if matrix[i][0] == 0:
                for c in range(n):
                    matrix[i][c] = 0

        for i in range(1, n):
            if matrix[0][i] == 0:
                for r in range(m):
                    matrix[r][i] = 0
        
        if firstColZero:
            for i in range(m):
                matrix[i][0] = 0
        
        if firstRowZero:
            for i in range(n):
                matrix[0][i] = 0