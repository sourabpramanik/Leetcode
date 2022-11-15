class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=nums[0]
        f=nums[0]
        
        s = nums[s]
        f = nums[nums[f]]
        while s!=f:
            s = nums[s]
            f = nums[nums[f]]
        
        f=nums[0]
        
        while s!=f:
            s = nums[s]
            f = nums[f]
        
        return s