class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        N=m+n-2
        r=n-1
        ans=1
        
        for i  in range(1, r+1):
            ans*= N-r+i
            ans //= i
        
        return ans