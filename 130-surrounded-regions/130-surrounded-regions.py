class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        def dfs(r, c):
            
            if r>=0 and c>=0 and r<len(board) and c<len(board[0]) and board[r][c] == "O":
            
                board[r][c] = "."
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)
        
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        for j in range(cols):
            dfs(0, j)
            dfs(rows-1, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == ".":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"