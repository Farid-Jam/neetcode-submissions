class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> rows[9];
        unordered_set<char> cols[9];
        unordered_set<char> boxes[9];

        for (int r = 0; r < board.size(); r++){
            for (int c = 0; c < board.size(); c++){
                if (board[r][c] == '.') continue;
                int boxIndex = (r / 3) * 3 + (c / 3);
                if (rows[r].count(board[r][c]) || cols[c].count(board[r][c]) || boxes[boxIndex].count(board[r][c])){
                    return false;
                }
                rows[r].insert(board[r][c]);
                cols[c].insert(board[r][c]);
                boxes[boxIndex].insert(board[r][c]);
            }
        }
        return true;
    }
};
