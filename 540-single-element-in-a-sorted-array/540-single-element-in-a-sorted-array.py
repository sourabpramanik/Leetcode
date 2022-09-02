class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        
        l, h=0, len(nums)-1
        
        while(l<h):
            mid=(l+h)//2
            
            if(nums[mid]==nums[mid^1]):
                l=mid+1
            else:
                h=mid
        return nums[l]