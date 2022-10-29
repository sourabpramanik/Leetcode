class Solution:
    def xorOperation(self, n: int, s: int) -> int:
        i=1
        start=s
        while i<n:
            start = start ^ (s + 2*i)
            i+=1
        
        return start