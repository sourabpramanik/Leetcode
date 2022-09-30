class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
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
        
        
        def unq(arr):
            
            for item in arr:                
                tup = tuple(item)
                if tup not in seen:
                    seen.add(tup)
                    yield item
        
        return list(unq(ans))
        