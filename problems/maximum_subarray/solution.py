class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        ans=float("-inf")
        curr=0
        
        for i in range(0, n):
            curr+=nums[i]
            ans=max(ans, curr)
            if curr<0:
                curr=0
                
        
        return ans