class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = []
        s = ""
        leftRow = []
        upDia = []
        lowDia = []
        for i in range(n):
            s +="."
            
        for i in range(n):
            board.append(s)
        
        for i in range(n):
            leftRow.append(0)
            
        for i in range(2*n):
            upDia.append(0)
        
        for i in range(2*n):
            lowDia.append(0)
        
        
        def rec(col, board):
            if col==n:
                ans.append(board[:])
                return
            
            for row in range(n):
                if(leftRow[row]==0 and lowDia[col+row]==0 and upDia[n-1+col-row]==0):
                    leftRow[row]=1
                    lowDia[col+row]=1 
                    upDia[n-1+col-row]=1
                    board[row] = board[row][:col] + "Q" + board[row][col+1:]
                                      
                    rec(col+1, board)
                    
                    leftRow[row]=0
                    lowDia[col+row]=0 
                    upDia[n-1+col-row]=0                    
                    board[row] = board[row][:col] + "." + board[row][col+1:]
        
        
        rec(0, board)
        
        return ans