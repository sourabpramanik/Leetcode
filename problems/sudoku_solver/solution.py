class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.rec(board, len(board))
    
    def rec(self, board, n):
        
        for i in range(0, n):
            for j in range(0, n):
                if board[i][j]==".":
                    for ch in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        if self.valid(board, i, j, ch):
                            board[i][j]=ch
                            if self.rec(board, n):
                                return True
                            else:
                                board[i][j]="."
                    return False
        return True
        
    def valid(self, board, row, col, ch):
        for i in range(0, 9):
            if board[row][i]==ch:
                return False
            
            if board[i][col]==ch:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==ch:
                return False
        return True

