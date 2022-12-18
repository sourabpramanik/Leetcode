class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast=nums[0]
        slow=nums[0]

        slow=nums[slow]
        fast=nums[nums[fast]]
        while fast!=slow:
            slow=nums[slow]
            fast=nums[nums[fast]]
        
        fast=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        
        return slow