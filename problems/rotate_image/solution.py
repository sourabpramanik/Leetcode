class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        for i in range(0, m):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(0, m):
            l=0
            r=n-1
            while l<=r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l+=1
                r-=1