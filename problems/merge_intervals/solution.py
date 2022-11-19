class Solution:
    def merge(self, mat: List[List[int]]) -> List[List[int]]:
        mat.sort(key=lambda x:x[0])
        n = len(mat)
        ans = []
        pair = mat[0]
        
        for i in range(0, n):
            if pair[1]>=mat[i][0]:
                pair[1] = max(pair[1], mat[i][1])
            else:
                ans.append(pair)
                pair = mat[i]
        ans.append(pair)
        return ans