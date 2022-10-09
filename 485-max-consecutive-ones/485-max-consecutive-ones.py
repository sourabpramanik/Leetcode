class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr=0
        maxi=float(-inf)
        
        i=0
        while i<len(nums):
            
            if nums[i]==1:
                curr+=1
            if nums[i]==0 or i==len(nums)-1:
                maxi=max(maxi, curr)
                curr=0
            i+=1
        return maxi