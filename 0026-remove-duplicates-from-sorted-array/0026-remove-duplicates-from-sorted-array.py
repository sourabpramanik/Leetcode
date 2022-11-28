class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        j=0
        n=len(nums)
        
        while i<n:
            if nums[i]!=nums[j]:
                j+=1
                nums[j]=nums[i]
            i+=1
        return j+1