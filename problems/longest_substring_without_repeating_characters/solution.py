class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        
        n = len(s)
        if n==0:
            return 0
        ans=0
        ds = set()
        l=0
        r=0
        while r<n:
            while l<r and s[r] in ds:                
                ds.remove(s[l])
                l+=1
                
            ans = max(ans, r-l+1)
            ds.add(s[r])
            r+=1
            
        
        return ans