class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        
        l, h=0, len(nums)-1
        
        while(l<h):
            mid=2 * ((l+h) // 4)
            
            if(nums[mid]==nums[mid+1]):
                l=mid+2
            else:
                h=mid
        return nums[l]