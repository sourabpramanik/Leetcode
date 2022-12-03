class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[0]*numRows
        
        for i in range(0, numRows):
            ans[i] = [0]*(i+1)
            ans[i][0]=1            
            ans[i][-1]=1
            for j in range(1, i):
                ans[i][j] = ans[i-1][j-1]+ans[i-1][j]
            
        return ans