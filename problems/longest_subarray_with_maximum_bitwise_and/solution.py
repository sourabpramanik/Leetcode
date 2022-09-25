class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m = max(nums)
        res = 0        
        for x, y in groupby(nums):
           
            if x == m:
                res = max(res, len(list(y)))
        return res