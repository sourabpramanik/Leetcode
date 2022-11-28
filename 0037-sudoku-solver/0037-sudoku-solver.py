class Solution:
    def solveSudoku(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """   
        
        self.solve(grid, len(grid))
        
    def solve(self, grid, n):
        for i in range(0, n):
            for j in range(0, n):
                if grid[i][j]==".":
                    for num in ["1","2","3","4","5","6","7","8","9"]:
                        if self.valid(grid, i, j, num):
                            grid[i][j] = num
                            if self.solve(grid, n):
                                return True
                            else:
                                grid[i][j] = "."
                    return False
        return True
                
    
    def valid(self, grid, row, col, char):
        for i in range(0, 9):
            if grid[i][col]==char:
                return False
            
            if grid[row][i]==char:
                return False
            if grid[3* (row//3) + (i//3)][3* (col//3) + (i%3)]==char:
                return False
        
        return True