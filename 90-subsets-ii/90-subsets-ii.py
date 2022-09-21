class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []        
        nums.sort()
        
        def rec(i, ds):
            ans.append(ds[:])
            
            for j in range(i, len(nums)):
                if(j>i and nums[j]==nums[j-1]):
                    continue
                
                ds.append(nums[j])
                rec(j+1, ds)
                ds.pop(len(ds)-1)
        rec(0, [])
        return ans
            