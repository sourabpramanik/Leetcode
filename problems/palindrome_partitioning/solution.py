class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        self.rec(0, [], s, len(s), ans)
        return ans
    
    def rec(self, i, ds, s, N, ans):
        if i>=N:
            ans.append(ds[:])
            return
        
        for j in range(i, N):
            if self.valid(s, i, j):
                ds.append(s[i:j+1])
                self.rec(j+1, ds, s, N, ans)
                ds.pop()
    
    def valid(self, s, l, r):
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True