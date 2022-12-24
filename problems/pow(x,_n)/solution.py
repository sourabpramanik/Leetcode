class Solution:
    def myPow(self, x: float, n: int) -> float:
        nn=n
        ans=1
        if n<0:
            nn=-1*nn
        
        while nn>0:
            if nn%2==0:
                x*=x
                nn/=2
            else:
                ans*=x
                nn-=1
        
        return ans if n>0 else float(1/ans)