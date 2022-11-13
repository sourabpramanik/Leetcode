class Solution:
    def getRow(self, n: int) -> List[int]:        
        ans = []
        for i in range(0, n+1):
            val = 1
            for j in range(0, i):
                val *= (n-j)
                val //= (j+1)
            ans.append(val)
        
        return ans
            