class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        n=len(nums)
        self.rec(0, nums, n, ans)
        return ans
    
    def rec(self, i, nums, N, ans):
        if i>=N:
            ans.append(nums[:])
            return
        
        for j in range(i, N):
            nums[i], nums[j] = nums[j], nums[i]
            self.rec(i+1, nums, N, ans)
            nums[i], nums[j] = nums[j], nums[i]
