class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        board=["."*n]*n
        left=[0]*n
        upDia=[0]*2*n
        lowDia=[0]*2*n

        def rec(j):
            if j == n:
                ans.append(board[:])
                return
            
            for i in range(0, n):
                if left[i]==0 and upDia[i+j]==0 and lowDia[n-1+j-i]==0:
                    left[i]=1 
                    upDia[i+j]=1
                    lowDia[n-1+j-i]=1                    
                    board[i]=board[i][:j]+"Q"+board[i][j+1:]
                    rec(j+1)
                    left[i]=0
                    upDia[i+j]=0
                    lowDia[n-1+j-i]=0 
                    board[i]=board[i][:j]+"."+board[i][j+1:]
        rec(0)

        return ans
    
    