class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        low=0
        high=n*m-1

        while low<=high:
            mid=(low+high)>>1
            val=matrix[mid//n][mid%n]
            if val==target:
                return True
            elif val>target:
                high=mid-1
            else:
                low=mid+1
        return False