class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def rec(i, ds):
            
            if len(ds)==k:
                ans.append(ds[:])
                return
            
            for j in range(i, n+1):
                ds.append(j)
                rec(j+1, ds)
                ds.pop(len(ds)-1)
        
        rec(1, [])
        
        return ans