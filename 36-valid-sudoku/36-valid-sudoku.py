class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validation check of row and column
        for i in range(len(board)):
            s1 = set()
            s2 = set()
            for j in range(len(board)):
                if board[i][j] != ".":   #row check
                    if board[i][j] in s1 :
                        return False
                    s1.add(board[i][j])
                if board[j][i] != ".":  # column check
                    if board[j][i] in s2:
                        return False
                    s2.add(board[j][i])
                
        # 3*3 grid  check        
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                s = set()                  # selecting per grid out of 9 by outer 2 loop
                for k in range(i, i+3,1):  # below 2 loop is used forlooping through per grid(3*3 matrix)
                    for l in range(j, j+3,1):
                        if  board[k][l]  in s:
                            return False
                        if board[k][l] != "." :
                            s.add(board[k][l])
                        
                        
        return True
        
                
                