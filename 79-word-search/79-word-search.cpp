class Solution {
    
    bool dfs(vector<vector<char>>& board, int r, int c, int index, string& word){
        if (index == word.size()) return true;
        if (r<0 || c<0 || r>=board.size() || c>=board[0].size() || word[index] != board[r][c]) return false;
        
        char ch = board[r][c];
        board[r][c] = '#';
        
        bool res = (dfs(board, r+1, c, index+1, word) || dfs(board, r-1, c, index+1, word) || dfs(board, r, c+1, index+1, word) || dfs(board, r, c-1, index+1, word));
        board[r][c] = ch;
        
        return res;
    }
public:
    bool exist(vector<vector<char>>& board, string word) {
        int rows = board.size();
        int cols = board[0].size();
        
        for(int i = 0; i<rows; i++){
            
            for(int j = 0; j<cols; j++){
                if (dfs(board, i, j, 0, word)) return true;
            }
        }
        return false;
        
    }
};