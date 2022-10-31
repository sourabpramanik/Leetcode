class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        setOne = 0
        setTwo = 0
        
        for num in nums:
            setOne = (setOne ^ num) & ~(setTwo)            
            setTwo = (setTwo ^ num) & ~(setOne)
        
        return setOne