class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        n=len(s)
        for i in range(0, n):
            temp=self.isValid(s, i, i)
            if len(temp)>len(ans):
                ans=temp
            
            temp=self.isValid(s, i, i+1)
            if len(temp)>len(ans):
                ans=temp

        return ans
    def isValid(self, s, l, r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]