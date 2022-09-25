class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        
        if len(a)==0:
            return False
        
        n = len(a)
        m = len(a[0])
        s = 0
        e = m*n-1
        
        while s<=e:
            mid = (s+e)//2
            
            if(a[mid//m][mid%m]==target):
                return True
            elif(a[mid//m][mid%m]>target):
                e=mid-1
            else:
                s=mid+1
        
        return False