class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        obj = dict()
        
        for v in nums:
            if v in obj:
                obj[v]+=1
            else:
                obj[v]=1
        
        maxi = float("-inf")
        key = 0
        for v in obj:          
            if maxi<obj[v]:
                maxi=obj[v]
                key=v
        return key