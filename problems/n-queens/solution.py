class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=["."*n]*n
        left=[0]*n
        up=[0]*2*n
        down=[0]*2*n
        ans=[]
        self.rec(board, 0, n, ans, left, up, down)
        return ans

    def rec(self, board, j, n, ans, left, up, down):
        if j>=n:
            ans.append(board[:])
            return
        
        for i in range(0, n):
            if left[i]==0 and up[n-1+j-i]==0 and down[j+i]==0:
                left[i]=1
                up[n-1+j-i]=1
                down[j+i]=1
                board[i] = board[i][:j]+"Q"+board[i][j+1:]
                self.rec(board, j+1, n, ans, left, up, down)
                left[i]=0
                up[n-1+j-i]=0
                down[j+i]=0
                board[i] = board[i][:j]+"."+board[i][j+1:]
    
    
