class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=0
        maxSum=float("-inf")
        
        for i in range(0, len(nums)):
            curSum+=nums[i]
            maxSum=max(maxSum, curSum)
            if curSum<0:
                curSum=0
        
        return maxSum