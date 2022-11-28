class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        flags={}
        
        for num in nums:
            flags[num]=False
            
        def rec(i, ds, flags):
            if i>=n:
                ans.append(ds[:])
                return
            
            for j in range(0, n):
                if flags[nums[j]]==False:
                    ds.append(nums[j])
                    flags[nums[j]]=True
                    rec(i+1, ds, flags)
                    ds.pop(len(ds)-1)
                    flags[nums[j]]=False
        
        rec(0, [], flags)
        return ans
                    