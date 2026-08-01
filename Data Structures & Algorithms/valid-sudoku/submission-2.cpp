class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> rows[9];
        unordered_set<char> cols[9];
        unordered_set<char> boxes[9];

        for (int row = 0; row < board.size(); ++row) {
            for (int col = 0; col < board.size(); ++col) {
                if (board[row][col] == '.') continue;
                char ch = board[row][col];
                int box = row / 3 * 3 + col / 3;
                if (rows[row].count(ch) || cols[col].count(ch) || boxes[box].count(ch)) {
                    return false;
                }
                rows[row].insert(ch);
                cols[col].insert(ch);
                boxes[box].insert(ch);
            }
        }
        return true;
    }
};
