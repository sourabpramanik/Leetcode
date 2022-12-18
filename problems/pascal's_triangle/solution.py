class Solution:
    def generate(self, num: int) -> List[List[int]]:
        
        ans=[0]*num

        for i in range(0, num):
            ans[i] = [0]*(i+1)
            ans[i][0]=1
            ans[i][-1]=1
            j=1
            while j<i:
                ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
                j+=1

        return ans 