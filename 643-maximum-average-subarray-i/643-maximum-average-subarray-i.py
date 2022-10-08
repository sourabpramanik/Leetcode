class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxi=float(-inf)
        currMax=0
        j=0
        for i in range(0, len(nums)):
            currMax += nums[i]
            
            if i>=k-1:
                maxi = max(maxi, currMax/k)
                currMax -= nums[j]
                j+=1
        
        return maxi