class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n=len(s)
        ans=0
        hs={}
        l=0
        for r in range(0, n):
            if s[r] in hs:
                l=max(l, hs[s[r]]+1)
            ans=max(ans, r-l+1)
            hs[s[r]]=r
        return ans
                