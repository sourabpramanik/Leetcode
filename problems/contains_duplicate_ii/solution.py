class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        m = {}
        
        while i<len(nums):
            if nums[i] in m and abs(i-m[nums[i]]<=k):
                return True
            m[nums[i]] = i                
            i+=1
        
        return False
            
        
        