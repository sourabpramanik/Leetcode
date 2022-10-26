class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mul=0
        m={0:0}
        for i in range(0, len(nums)):
            mul += nums[i]
            
            key = mul%k
            
            if not key in m:
                m[key] = i+1
                
            elif m[key]<i:
                return True
                
        
        return False