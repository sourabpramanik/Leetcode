class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            diff=target-nums[i]
            low=i+1
            high=len(nums)-1

            while low<=high:
                mid=(low+high)>>1
                if nums[mid]==diff:
                    return [i+1, mid+1]
                elif nums[mid]>diff:
                    high=mid-1
                else:
                    low=mid+1
        return [-1, -1]

