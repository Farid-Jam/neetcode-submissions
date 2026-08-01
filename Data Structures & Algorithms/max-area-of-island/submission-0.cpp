class Solution {
    int directions[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int maxArea = 0;
        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                if (grid[r][c] == 1){
                    int islandArea = dfs(grid, r, c);
                    maxArea = max(maxArea, islandArea);
                }
            }
        }
        return maxArea;
    }

    int dfs(vector<vector<int>>& grid, int r, int c){
        if (r >= grid.size() || c >= grid[0].size() || r < 0 || c < 0 || grid[r][c] == 0){
            return 0;
        }
        grid[r][c] = 0;
        int area = 1; 
        for (int i = 0; i < 4; i++){
            area += dfs(grid, r + directions[i][0], c + directions[i][1]);
        }
        return area;
    }
};
