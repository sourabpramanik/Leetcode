class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        
        if len(a)==0:
            return False
        
        m = len(a)
        n = len(a[0])
        r = 0
        c = n-1
        
        while r<m and c>=0:
            if(a[r][c]==target):
                return True
            elif(a[r][c]>target):
                c-=1
            else:
                r+=1
        return False