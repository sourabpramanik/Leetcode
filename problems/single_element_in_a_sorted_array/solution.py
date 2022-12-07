class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-2
        ans=0
        while l<=h:
            mid=(l+h)>>1

            if nums[mid]==nums[mid^1]:
                l=mid+1
            else:                
                h=mid-1

        return nums[l]               