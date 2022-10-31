class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        
        for i in range(0, len(mat)-1):
            for j in range(0, len(mat[0])-1):
                if mat[i][j]!=mat[i+1][j+1]:
                    return False
        
        return True