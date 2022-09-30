class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans=[]
        
        def rec(i, ds, rem):
            if len(ds)==k:
                if rem==0:
                    ans.append(ds[:])
                return
            
            if i>=n:
                return
            
            if rem>=i:
                for j in range(i+1, 10):
                    if j>i and j==j-1:
                        continue
                    
                    ds.append(j)
                    rem-=j
                    rec(j, ds, rem)
                    rem+=j
                    ds.pop(len(ds)-1)
            
        rec(0, [], n)
        
        return ans