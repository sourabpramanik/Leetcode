class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n=len(s)
        l=0
        r=0
        ds={}
        while r<n:
            if s[r] in ds:
                l = max(l,ds[s[r]]+1)
                
            ds[s[r]] = r
            ans = max(ans, r-l+1)
            r+=1
            
                
        
        return ans