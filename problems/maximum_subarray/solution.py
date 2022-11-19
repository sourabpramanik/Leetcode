class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        n = len(nums)
        currSum=0
        for i in range(0, n):
            currSum += nums[i]            
            ans = max(ans, currSum)
            if currSum <0:
                currSum = 0
                
        
        return ans
                
        