class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        map = collections.defaultdict(list)
        
        m = len(mat)
        n = len(mat[0])
        
        for i in range(0, m):
            for j in range(0, n):
                map[i-j].append(mat[i][j])
        
        for k in map:
            map[k].sort()
        
        for i in range(0, m):
            for j in range(0, n):
                mat[i][j] = map[i-j].pop(0)
        
        return mat