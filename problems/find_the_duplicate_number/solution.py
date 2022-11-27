class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = nums[0], nums[0]
        
        fast=nums[nums[fast]]
        slow=nums[slow]
        while fast!=slow:
            fast=nums[nums[fast]]
            slow=nums[slow]
        
        fast=nums[0]
        
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        
        return slow