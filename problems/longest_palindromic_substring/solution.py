class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        ans=""
        for i in range(0, n):
            temp = self.valid(i, i, s)
            if len(temp)>len(ans):
                ans=temp
            
            temp = self.valid(i, i+1, s)
            if len(temp) > len(ans):
                ans=temp
        
        return ans
    def valid(self, l, r, s):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]