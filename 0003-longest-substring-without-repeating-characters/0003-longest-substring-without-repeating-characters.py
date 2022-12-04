class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        n=len(s)
        i=0
        j=0
        ds=set()
        while j<n:
            if s[j] in ds:
                ds.remove(s[i])
                i+=1
            else:
                ans=max(ans, j-i+1)
                ds.add(s[j])
                j+=1
        
        return ans