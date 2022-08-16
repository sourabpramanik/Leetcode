class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        
        if len(s)<3: return 0
        
        count = 0
        a, b, c = s[0], s[1], s[2]
        
        i=3
   
        
        while i<len(s):
            if a!=b and b!=c and c!=a: 
                count+=1
                print(a,b,c)
            a = b
            b = c
            c = s[i]
            i+=1                                                
        
        if a!=b and b!=c and c!=a: 
                count+=1
        return count