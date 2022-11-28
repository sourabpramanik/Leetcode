class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans=0
        grid=["."*n]*n
        leftCol=[0]*n
        upDia=[0]*2*n
        lowDia=[0]*2*n
        
        def rec(j, grid):
            if j==n:
                self.ans+=1
                return
            
            for i in range(n):
                if leftCol[i]==0 and upDia[j+i]==0 and lowDia[n-1+j-i]==0:
                    leftCol[i]=1
                    upDia[i+j]=1
                    lowDia[n-1+j-i]=1
                    grid[i]=grid[i][:j]+"Q"+grid[i][j+1:]
                                        
                    rec(j+1, grid)
                    
                    leftCol[i]=0
                    upDia[i+j]=0
                    lowDia[n-1+j-i]=0
                    grid[i]=grid[i][:j]+"."+grid[i][j+1:]
        rec(0, grid)
        
        return self.ans 