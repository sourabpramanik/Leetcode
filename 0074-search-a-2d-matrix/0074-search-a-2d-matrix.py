class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        
        for i in range(0, m):
            if matrix[i][-1]>=target:
                l=0
                r=n
                
                while(l<r):
                    mid = (l+r)//2
                    if matrix[i][mid]==target:
                        return True
                    elif matrix[i][mid]>target:
                        r-=1
                    else:
                        l+=1
        return False