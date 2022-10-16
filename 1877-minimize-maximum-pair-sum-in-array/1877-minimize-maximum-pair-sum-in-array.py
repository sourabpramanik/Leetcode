class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        maxi = float(-inf)
        curr = 0
        nums.sort()
        i=0
        j=len(nums)-1
        
        while(i<j):
            curr = nums[i]+nums[j]
            maxi = max(curr, maxi)
            i+=1
            j-=1
            
        return maxi
            