class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float("-inf")
        curSum=0
        
        for v in nums:
            curSum+=v
            if maxSum<curSum:
                maxSum=curSum
            if curSum<0:
                curSum=0
        return maxSum