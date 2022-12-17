class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        m = {}
        for ch in s:
            m[ch]=m.get(ch, 0)+1
        
        for ch in t:
            if not ch in m:
                return False
            m[ch]-=1
        
        for key in m:
            if m[key]>0:
                return False
        
        return True