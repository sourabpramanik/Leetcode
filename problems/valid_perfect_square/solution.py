class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 1
        e = 2**31-1
        
        while s<=e:
            mid = (s+e)//2
            if mid**2==num:
                return True
            elif mid**2>num:
                e=mid-1
            else:
                s=mid+1
        return False