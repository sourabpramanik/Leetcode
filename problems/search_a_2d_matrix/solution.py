class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        
        i=0
        j=(m*n)-1
        while i<=j:
            mid = (i+j)//2
            val = matrix[mid//n][mid%n]
            if val==target:
                return True
            elif val>target:
                j=mid-1
            else:
                i=mid+1
        return False
                