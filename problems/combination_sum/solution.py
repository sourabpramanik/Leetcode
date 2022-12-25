class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        self.rec(0, [], candidates, target, len(candidates), ans)
        return ans
    
    def rec(self, i, ds, C, target, N, ans):
        if target==0:
            ans.append(ds[:])
            return

        if i>=N:
            return

        if target>=C[i]:
            ds.append(C[i])
            self.rec(i, ds, C, target-C[i], N, ans)
            ds.pop()
        self.rec(i+1, ds, C, target, N, ans)
        
