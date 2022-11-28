class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans=[]
        grid=["."*n]*n        
        
        def rec(j, grid):
            if j==n:
               
                ans.append(grid[:])
                return 
            
            for i in range(n):
                if self.safe(i, j, grid):                   
                    grid[i]=grid[i][:j]+"Q"+grid[i][j+1:]                    
                    rec(j+1, grid)                    
                    grid[i]=grid[i][:j]+"."+grid[i][j+1:]
        rec(0, grid)
        
        return ans      
    
    def safe(self, row, col, grid):
        i=row
        j=col
        
        while i>=0 and j>=0:
            if grid[i][j]=="Q":
                return False
            i-=1
            j-=1
        
        
        j=col
        
        while j>=0:
            if grid[row][j]=="Q":
                return False            
            j-=1
        
        i=row
        j=col
        while i<len(grid) and j>=0:
            if grid[i][j]=="Q":
                return False
            i+=1
            j-=1
        
        return True