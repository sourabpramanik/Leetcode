class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(0, (1<<len(nums))):
            ds = []
            for j in range(0, len(nums)):
                if i&(1<<j):
                    ds.append(nums[j])
            ans.append(ds)
        
        return ans
    