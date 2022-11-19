class Solution:
    def merge(self, mat: List[List[int]]) -> List[List[int]]:
        mat.sort(key=lambda x:x[0])
        n = len(mat)
        ans = [mat[0]]
        i=0
        for i in range(0, n):
            start = mat[i][0]            
            end = mat[i][-1]
            
            if start <= ans[-1][-1]:
                ans[-1][-1] = max(ans[-1][-1], end)
                continue
            for j in range(i+1, 0):
                if mat[j][0]<=end:
                    end = max(mat[j][-1], end)
            
            end = max(end, mat[i][-1])
            ans.append([start, end])
           
        return ans