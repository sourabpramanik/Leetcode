class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        curr=1
        ans=1
        prev=nums[0]
        for i in range(1, len(nums)):
            if nums[i]==prev+1:
                curr+=1
            elif nums[i]!=prev:
                curr=1
            prev = nums[i]            
            ans = max(ans, curr)
        return ans