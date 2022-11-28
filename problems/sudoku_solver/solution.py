class Solution:
    def solveSudoku(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """   
        self.grid = grid
        self.n = len(grid)
        self.solve()
        
    def solve(self):
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.grid[i][j]==".":
                    for num in ["1","2","3","4","5","6","7","8","9"]:
                        if self.valid(i, j, num):
                            self.grid[i][j] = num
                            if self.solve():
                                return True
                            else:
                                self.grid[i][j] = "."
                    return False
        return True
                
    
    def valid(self, row, col, char):
        for i in range(0, 9):
            if self.grid[i][col]==char:
                return False
            
            if self.grid[row][i]==char:
                return False
            if self.grid[3* (row//3) + (i//3)][3* (col//3) + (i%3)]==char:
                return False
        
        return True