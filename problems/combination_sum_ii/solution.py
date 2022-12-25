class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        candidates.sort()
        self.rec(0, [], candidates, target, len(candidates), ans)
        return ans
    
    def rec(self, i, ds, candidates, target, N, ans):
        if target==0:
            ans.append(ds[:])
            return 
        
        if i>=N:
            return
        
        if target>=candidates[i]:
            for j in range(i, N):
                if target<candidates[j]:
                    break
                if j>i and candidates[j]==candidates[j-1]:
                    continue

                ds.append(candidates[j])
                target-=candidates[j]
                self.rec(j+1, ds, candidates, target, N, ans)
                target+=candidates[j]
                ds.pop()
