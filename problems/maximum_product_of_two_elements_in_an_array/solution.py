class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m1=0
        m2=0
        
        for v in nums:
            if v > m1:
                m2 = m1
                m1 = v
                
            else:
                m2 = max(m2, v)
        
        return (m1-1)*(m2-1)