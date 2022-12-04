class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n=len(nums)
        ds={}
        for i in range(0, n):
            val = target-nums[i]
            if val in ds:
                return [ds[val], i]
            else:
                ds[nums[i]] = i
        
        return[-1, -1]
        
        