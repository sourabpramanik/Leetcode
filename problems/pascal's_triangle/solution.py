class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans=[0]*n
        ans[0]=[1]
        for i in range(1, n):
            ans[i] = [0]*(i+1)
            ans[i][0]=1            
            ans[i][-1]=1
            for j in range(1, i):
                ans[i][j]=ans[i-1][j-1] + ans[i-1][j]
        
        return ans