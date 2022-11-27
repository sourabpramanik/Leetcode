class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        prev=nums[0]
        count=1
        ans=1
        for i in range(1, len(nums)):
            curr=nums[i]
            if curr==prev+1:
                count+=1
            elif curr!=prev:
                count=1
            ans = max(count, ans)
            prev=curr
        
        return ans