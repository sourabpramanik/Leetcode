class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        res = [0]*len(grid[0])
        for i in range(0, len(grid[0])):
            res[i] = self.dropCol(0, i, grid)
    
        return res
    
    def dropCol(self, row, col, grid):
        if row == len(grid):
            return col
        
        nextCol = col + grid[row][col]
        if nextCol < 0 or nextCol > len(grid[0])-1 or grid[row][col] != grid[row][nextCol]:
            return -1
        
        return self.dropCol(row+1, nextCol, grid)