class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashMap=Counter(nums)
        ans=0
       
        
        for i in range(0, len(nums)):
            curr=nums[i]
            count=1
            if not curr-1 in hashMap:
                p=curr+1
                while p in hashMap:
                    count+=1
                    p+=1     
            ans=max(ans, count)

        return ans