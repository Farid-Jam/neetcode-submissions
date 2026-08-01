class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> rows[9];
        unordered_set<char> cols[9];
        unordered_set<char> boxes[9];
        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                if (board[i][j] == '.') {
                    continue;
                }
                if (rows[i].count(board[i][j])) {
                    return false;
                } else {
                    rows[i].insert(board[i][j]);
                }
                if (cols[j].count(board[i][j])) {
                    return false;
                } else {
                    cols[j].insert(board[i][j]);
                } 
                if (boxes[i / 3 * 3 + j / 3].count(board[i][j])){
                    return false;
                } else {
                    boxes[i / 3 * 3 + j / 3].insert(board[i][j]);
                }
            }
        }
        return true;
    }
};
