class Solution:
    def generate(self, n: int) -> List[List[int]]:
        v = [0]*n
        
        for i in range(0, n):
            v[i] = [0]*(i+1)
            v[i][0]=1
            v[i][-1]=1
            for j in range(1, i):
                v[i][j] = v[i-1][j-1] + v[i-1][j]
        
        return v