class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def isPal(val, l, r):            
            
            while l<=r:
                if val[l]!=val[r]:
                    return False
                l+=1
                r-=1
            return True
        
        def rec(i, ds):
            if i>=len(s):
                res.append(ds[:])
                return
            
            for j in range(i, len(s)):
                if isPal(s, i, j):
                    ds.append(s[i:j+1])
                    rec(j+1, ds)
                    ds.pop(len(ds)-1)
        
        rec(0, [])
            
        return res