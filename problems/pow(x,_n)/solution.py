class Solution:
    def myPow(self, x: float, n: int) -> float:
        p=n
        ans=1
        if n<0:
            p = -1*n
        
        while p>0:
            if p%2==0:
                x *= x
                p = p//2
            else:
                ans *= x
                p = p-1
        
        return ans if n>0 else float(1/ans)