class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        l=1
        h=x
        
        while True:
            mid = (l+h)//2
            
            if mid>x/mid:
                h=mid-1            
            else:
                if mid+1 > x/(mid+1):
                    return mid
                l=mid+1
             