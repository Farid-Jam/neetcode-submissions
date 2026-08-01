class Solution {
    int directions[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
private:
    int dfs(vector<vector<int>>& grid, int r, int c) {
        if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size() || grid[r][c] == 0) {
            return 0;
        }
        grid[r][c] = 0;
        int size = 1;
        for (int i = 0; i < 4; i++) {
            size += dfs(grid, r + directions[i][0], c + directions[i][1]);
        }
        return size;
    }
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int row = grid.size(), col = grid[0].size(), biggest = 0;
        for (int r = 0; r < row; r++){
            for(int c = 0; c < col; c++){
                if (grid[r][c] == 1) {
                    biggest = max(biggest, dfs(grid, r, c));
                }
            }
        }
        return biggest;
    }
};
