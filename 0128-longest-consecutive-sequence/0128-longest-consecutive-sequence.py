class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxi=1
        curr=1
        
        nums.sort()
        n=len(nums)
        prev=nums[0]
        for i in range(1,n):
            if prev+1==nums[i]:
                curr+=1
            elif prev!=nums[i]:
                curr=1
            prev=nums[i]
            maxi=max(curr, maxi)
        
        return maxi