class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        n = len(s)
        if n==0:
            return 0
        ans=0
        ds = {}
        l=0
        r=0
        while r<n:
            if l<r and s[r] in ds:                
                l = max(l, ds[s[r]]+1)
                
            ans = max(ans, r-l+1)
            ds[s[r]] = r
            r+=1
            
        
        return ans