class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                if board[i][j]  in s:
                    return False
                if board[i][j] != "." and board[i][j]  not in s:
                    s.add(board[i][j])
                
        for i in range(len(board)):
            s = set()
            for j in range(len(board)):
                if board[j][i]  in s:
                    return False
                if board[j][i] != "." and board[j][i]  not in s:
                    s.add(board[j][i])
                
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                s = set()
                for k in range(i, i+3,1):
                    for l in range(j, j+3,1):
                        if  board[k][l]  in s:
                            return False
                        if board[k][l] != "." and board[k][l]  not in s:
                            s.add(board[k][l])
                        
                        
        return True
        
                
                