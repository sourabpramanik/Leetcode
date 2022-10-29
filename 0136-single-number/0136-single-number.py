class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for v in nums:
            xor ^= v
        
        return xor