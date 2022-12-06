class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact=1
        arr=[]
        ans=""
        for i in range(1, n):
            fact*=i
            arr.append(i)
        arr.append(n)
        k=k-1

        while True:
            id=k//fact
            ans+=str(arr[id])
            arr.pop(id)
            if len(arr)==0:
                break
            k=k%fact
            fact//=len(arr)
            
        
        return ans