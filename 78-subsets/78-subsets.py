class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        def rec(i, ds):
            if i>=len(nums):
                ans.append(ds[:])
                return
                        
            ds.append(nums[i])
            rec(i+1, ds)
            ds.pop(len(ds)-1)
            rec(i+1, ds)
        
        rec(0, [])
        return ans