class Solution:
    def check(self, nums: List[int]) -> bool:
        
        
        n=len(nums)
        x=0
        for i in range(1, n):
            if nums[i-1]>nums[i]:
                x+=1
        
        return x==0 or x==1 and nums[0]>=nums[-1]