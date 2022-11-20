class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(0, m):
            l=0
            r=n-1
            while l<=r:
                mid = (l+r)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    r = mid-1
                else:
                    l = mid+1
        return False