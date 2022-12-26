class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1

        while l<=h:
            mid=(l+h)>>1
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[l]:
                if target>=nums[l] and target<=nums[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if target>=nums[mid] and target<=nums[h]:
                    l=mid+1
                else:
                    h=mid-1
        return -1