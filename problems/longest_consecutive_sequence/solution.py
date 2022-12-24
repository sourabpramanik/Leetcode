class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashes={}
        n=len(nums)
        sub=0

        for num in nums:
            hashes[num]=1
        for i in range(0, n):
            if nums[i]-1 not in hashes:
                val=nums[i]
                count=0
                while val in hashes:
                    count+=1
                    val+=1
                sub=max(sub, count)
        
        return sub

