class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        n=len(s)
        def rec(i, ds):
            if i>=n:
                ans.append(ds[:])
                return
            
            for j in range(i, n):
                if self.pal(s, i, j):
                    ds.append(s[i:j+1])
                    rec(j+1, ds)
                    ds.pop()
        
        rec(0, [])
        return ans
    
    def pal(self, s, i, j):
        l=i
        r=j
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
