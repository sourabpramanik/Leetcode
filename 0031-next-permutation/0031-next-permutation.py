class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-1
        while i>=0:
            if i<len(nums)-1 and nums[i]<nums[i+1]:
                break
            i-=1
        
        j = len(nums)-1
        
        if i>=0:
            while j>=0:
                if nums[i]<nums[j]:
                    break
                j-=1

            nums[i], nums[j] = nums[j], nums[i]
        
        i=i+1
        j=len(nums)-1
        
        while i<=j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
            
        
            