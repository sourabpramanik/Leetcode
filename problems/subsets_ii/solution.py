class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        self.rec(0, [], nums, len(nums), ans)
        return ans
    def rec(self, i, ds, nums, N, ans):
        ans.append(ds[:])
        if i>=N:
            return
        for j in range(i, N):
            if j>i and nums[j]==nums[j-1]:
                continue
            ds.append(nums[j])
            self.rec(j+1, ds, nums, N, ans)
            ds.pop()