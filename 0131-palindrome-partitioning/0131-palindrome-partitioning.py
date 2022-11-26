class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        n=len(s)
        def rec(i, ds, s):
            if i>=n:
                ans.append(ds[:])
                return
            
            for j in range(i, n):
                if self.check(i,j,s):
                    ds.append(s[i:j+1])
                    rec(j+1, ds, s)
                    ds.pop(len(ds)-1)
        rec(0, [], s)
        return ans
    def check(self, l, r, s):
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True