class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        m = n
        
        while m:
            if m%2==0 and m%n==0:
                return m
            m+=1
                
        