class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashMap = {}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0)+1
        
        i=0
        while i<len(nums):
            if 0 in hashMap and hashMap[0]>0:
                nums[i]=0
                hashMap[0]-=1
            elif 1 in hashMap and hashMap[1]>0:
                nums[i]=1
                hashMap[1]-=1
            elif 2 in hashMap and hashMap[2]>0:
                nums[i]=2
                hashMap[2]-=1
        
            i+=1
            
        
                