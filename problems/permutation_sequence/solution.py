class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans=""
        ds=[]
        fact=1
        
        for i in range(1, n):
            ds.append(i)
            fact = fact*i
        
        ds.append(n)
        k=k-1
        
        while True:
            ans = ans + str(ds[k//fact])
            ds.pop(k//fact)
            if len(ds)==0:
                break
            k=k%fact
            fact = fact//len(ds)
        
        return ans