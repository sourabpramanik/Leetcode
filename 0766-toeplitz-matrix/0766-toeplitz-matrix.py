class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        
        # for i in range(0, len(mat)):
        #     for j in range(0, len(mat[0])):
        #         if i>0 and j >0 and mat[i][j]!=mat[i-1][j-1]:
        #             return False
        
        return all(r1[:-1] == r2[1:] for r1,r2 in zip(mat, mat[1:]))