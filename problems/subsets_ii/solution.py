class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        n=len(nums)
        nums.sort()
        def rec(i, ds):
            
            if i>=n:
                ans.add(tuple(ds[:]))
                return 
            
            ds.append(nums[i])
            rec(i+1, ds)
            ds.pop()
            rec(i+1, ds)
            
        rec(0, [])
        return ans