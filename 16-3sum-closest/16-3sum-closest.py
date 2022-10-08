class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        result = nums[0]+nums[1]+nums[2]
        for i in range(1, len(nums)):
            j=i+1
            k=len(nums)-1
            
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if abs(s-target)<abs(result-target):
                    result=s
                if s > target:
                    k-=1
                else:
                    j+=1
            
        
        return result