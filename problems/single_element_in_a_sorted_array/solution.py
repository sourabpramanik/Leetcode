class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        h=n-2
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==nums[mid^1]:
                l=mid+1
            else:
                h=mid-1
        return nums[l]