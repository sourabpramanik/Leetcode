class Solution:
    def combinationSum2(self, C: List[int], T: int) -> List[List[int]]:
        C.sort()
        ans=[]
        
        def rec(i, ds, rem):
            if rem==0:
                ans.append(ds[:])
                return
            
            if i>=len(C):
                return
            for j in range(i, len(C)):
                if j>i and C[j] == C[j-1]:
                    continue
                if rem>=C[i]:                
                    ds.append(C[j])
                    rem-=C[j]
                    rec(j+1, ds, rem)
                    rem+=C[j]
                    ds.pop(len(ds)-1)            
                
                
        
        rec(0, [], T)
        
        return ans