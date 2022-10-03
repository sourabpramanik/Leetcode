class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        
        return n==1 or (n%3==0 and self.isPowerOfThree(n/3))