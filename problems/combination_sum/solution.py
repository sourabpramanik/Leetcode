class Solution:
    def combinationSum(self, A: List[int], target: int) -> List[List[int]]:
        n=len(A)
        ans=[]
        def rec(id, ds, targetSum):
            if targetSum==0:
                ans.append(ds[:])
                return

            if id>=n:
                return                         
            
            if targetSum>=A[id]:
                ds.append(A[id])
                rec(id, ds, targetSum-A[id])
                ds.pop()
            rec(id+1, ds, targetSum)

        rec(0, [], target)
        return ans            