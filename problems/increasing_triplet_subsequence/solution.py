class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a=float("inf")
        b=float("inf")
        
        for e in nums:
            if e<=a:
                a=e
            elif e<=b:
                b=e
            else:
                return True
           
        return False