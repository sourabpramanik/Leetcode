class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(0, n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j]=matrix[i][j], matrix[j][i]
        
        
        for i in range(0, n):
            l=0
            r=n-1
            while(l<=r):
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l+=1
                r-=1
                