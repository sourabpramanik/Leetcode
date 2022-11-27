class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashMap={}
        for num in nums:
            hashMap[num] = hashMap.get(num, 0)+1
        
        for k in hashMap:
            if hashMap[k]>1:
                return k
        
        return -1