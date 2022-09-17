class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = nums[0]+nums[1]+nums[2]
        nums.sort()
        i=0
        while i<len(nums)-1:
            j=i+1
            k=len(nums)-1
            
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                
                if s==target:
                    return s
                if abs(s-target) < abs(result-target):
                    result  = s
                
                if s > target:
                    k-=1
                if s< target:
                    j+=1
            
            i+=1
        
        return result