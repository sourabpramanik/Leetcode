class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        
        return n==1 or (n%4==0 and self.isPowerOfFour(n/4))