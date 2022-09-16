class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        
        while sum(res) <= sum(nums):
            res.append(nums.pop())
        
        return res