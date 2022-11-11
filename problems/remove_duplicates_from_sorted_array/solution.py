class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=0
        while j<len(nums):
            while j+1<len(nums) and nums[j+1]==nums[j]:
                j+=1
            
            nums[i]=nums[j]
            i+=1
            j+=1
        
        return i
        
        