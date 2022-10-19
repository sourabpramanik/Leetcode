class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        res = 0
        
        while True:
            a, b, c = sorted([a, b, c])
            
            if a>0:
                a-=1
                c-=1
                res+=1
            elif b>0:
                b-=1
                c-=1
                res+=1
            
            else:
                break
        
        return res