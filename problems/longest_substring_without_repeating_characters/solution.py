class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        n=len(s)
        i=0
        j=0
        ds={}
        while j<n:
            if s[j] in ds:                
                i=max(i, ds[s[j]]+1)
            
            ans=max(ans, j-i+1)
            ds[s[j]] = j
            j+=1
        
        return ans