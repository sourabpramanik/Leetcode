class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count=0
#         BRUTE
        while a or b or c:
            bitA = a&1            
            bitB = b&1            
            bitC = c&1
            
            if (bitA|bitB)!=bitC:
                if bitA==1 and bitB==1:
                    count+=2
                else:
                    count+=1
            a = a>>1            
            b = b>>1           
            c = c>>1
        
        return count