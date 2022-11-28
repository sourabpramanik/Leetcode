class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        def rec(i, ds):
            if i>=n:
                ans.append(ds[:])
                return
            
            for j in range(i, n):
                ds[i], ds[j] = ds[j], ds[i]
                rec(i+1, ds)
                ds[i], ds[j] = ds[j], ds[i]
                
        rec(0, nums)
        return ans
