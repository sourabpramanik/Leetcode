class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def rec(ds, freq):
            if len(ds)==n:
                ans.append(ds[:])
                return
            
            for i in range(0, n):
                if not freq[i]:
                    freq[i] = True
                    ds.append(nums[i])
                    rec(ds, freq)
                    ds.pop(len(ds)-1)
                    freq[i] = False
         
        freq = {}
        for i in range(0, n):
            freq[i]=False
        
        rec([], freq)
        return ans