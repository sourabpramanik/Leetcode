class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(0,n):            
            ans += [x+(1<<i) for x in reversed(ans)]
        
        return ans