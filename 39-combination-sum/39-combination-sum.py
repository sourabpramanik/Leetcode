class Solution:
    def combinationSum(self, A, tar) -> List[List[int]]:
        
        ans = []
        def rec(i, ds, rem):
            if rem==0:
                ans.append(ds[:])
            
            if rem<=0: return
            if i>=len(A): return
            
            if rem>=A[i]:
                ds.append(A[i])
                rem-=A[i]
                rec(i, ds, rem)
                rem+=A[i]
                ds.pop(len(ds)-1)
                
            rec(i+1, ds, rem)
            
        
        rec(0, [], tar)
        
        return ans