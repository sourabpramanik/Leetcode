class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t)>len(s):
            return ""
        l=0
        ans=""
        m=Counter(t)
        w=Counter()
            
        for r in range(0, len(s)):
            w[s[r]] = w.get(s[r], 0) + 1            
            while w >= m:
                if ans == "" or r - l <len(ans):
                    ans = s[l:r+1]
                w[s[l]] -= 1
                l+=1                    
        return ans
                
