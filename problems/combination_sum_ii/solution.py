class Solution:
    def combinationSum2(self, A: List[int], target: int) -> List[List[int]]:
        ans=[]
        n=len(A)
        A.sort()
        def rec(i, ds, target):
            if target==0:
                ans.append(ds[:])
                return
            
            if i>=n:
                return

            for j in range(i, n):
                if target<A[j]:
                    break
                if j>i and A[j]==A[j-1]:
                    continue
                ds.append(A[j])
                rec(j+1, ds, target-A[j])
                ds.pop()                
            
        
        rec(0, [], target)
        return ans