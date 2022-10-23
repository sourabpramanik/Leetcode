class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        m = {}
        
        for i in range(0, len(nums)):
            m[i+1] = 0
        
        for v in nums:
            m[v] += 1 
        
        ans = [0]*2
        
        for k in m:
            if m[k]==2:
                ans[0]=k
            if m[k]==0:
                ans[1]=k
        
        return ans
        