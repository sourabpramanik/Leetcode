class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        element=0
        
        for i in range(0, len(nums)):
            if count==0:
                element = nums[i]
                
            if element==nums[i]:
                count+=1
            else:
                count-=1
        
        return element