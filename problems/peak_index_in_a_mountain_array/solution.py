class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:

        n=len(nums)

        low=0
        high=n-1

        while low<=high:
            mid=(low+high)>>1

            if nums[mid]<nums[mid+1]:
                low=mid+1
            else:
                high=mid-1

        return low 