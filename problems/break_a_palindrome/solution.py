class Solution:
    def breakPalindrome(self, P: str) -> str:
        if len(P)==1:
            return ""
        for i in range(0, len(P)//2):
            if P[i]!="a":
                return P[:i] + "a" + P[i+1:]
        return P[:-1]+"b"