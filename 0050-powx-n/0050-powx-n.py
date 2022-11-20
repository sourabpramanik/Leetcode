class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        nn=n
        if n<0:
            nn= -1 * n
        
        while nn>0:
            if nn%2:
                ans = ans * x
                nn = nn - 1
            else:
                x = x*x
                nn = nn/2
        return float(ans) if n>0 else 1/float(ans)