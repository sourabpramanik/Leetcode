class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row=[1]*m
        col=[1]*n
        for i in range(0, m):
            for j in range(0,n):
                if matrix[i][j]==0:
                    row[i]=0
                    col[j]=0
        
        
        for i in range(0, m):
            for j in range(0,n):
                if row[i]==0 or col[j]==0:
                    matrix[i][j]=0   
        
        