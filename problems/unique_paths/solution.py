class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = n+m-2
        downs=n-1
        ans=1
        for i in range(0, downs):
            ans = ans * (directions-downs+(i+1))
            ans //= i+1
        
        return ans