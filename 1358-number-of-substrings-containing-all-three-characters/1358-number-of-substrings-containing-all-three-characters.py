class Solution:
    def numberOfSubstrings(self, w: str) -> int:
        f = {"a":0, "b":0, "c":0}        
        s=0
        res=0
        
        for e in range(0, len(w)):
            f[w[e]]+=1
            
            while all(f.values()):
                f[w[s]]-=1
                s+=1
            res+=s
        
        return res
            
        