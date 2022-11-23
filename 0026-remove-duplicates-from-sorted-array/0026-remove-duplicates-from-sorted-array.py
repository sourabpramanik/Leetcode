class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hs=set()
        for i in range(0, len(nums)):
            hs.add(nums[i])
        
        k=len(hs)
        hs=sorted(hs)
        j=0
        for val in hs:
            nums[j]=val
            j+=1
            
        return k
        