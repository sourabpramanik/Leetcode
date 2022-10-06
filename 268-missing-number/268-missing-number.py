class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = []
        
        for _ in range(0, len(nums)+1):
            arr.append(0)
            
        for i in range(0,len(nums)):
            arr[nums[i]]+=1
        
        for v in arr:
            if v==0:
                return arr.index(v)