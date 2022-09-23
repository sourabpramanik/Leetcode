class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def isPal(s, l, r):
            while l<=r:
                if(s[l]!=s[r]):
                    return False
                l+=1
                r-=1
            return True
        
        def rec(s, ind, path):
            if ind==len(s):
                res.append(path[:])
                return
            
            for i in range(ind, len(s)):
                if(isPal(s, ind, i)):
                    path.append(s[ind:i+1])
                    rec(s, i+1, path)
                    path.pop(len(path)-1)
        
        rec(s, 0, [])
        
        return res