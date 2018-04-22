class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.solve(0,0,board)
    
    
    
    def solve(self,i,j,board):
        if i == len(board):
            return True
        
        if j == len(board[0]):
            return self.solve(i+1,0,board)
        
        if board[i][j] != '.':
            return self.solve(i,j+1,board)
        
        for n in '123456789':
            if not self.valid(n,i,j,board):
                continue
            board[i][j] = n
            if self.solve(i,j+1,board):
                return True
            else:
                board[i][j] = '.'
                
        return False
            
            
    def valid(self,n,i,j,board):
        for k in range(9):
            if board[i][k] != '.' and board[i][k] == n:
                return False
            if board[k][j] != '.' and board[k][j] == n:
                return False
            if board[3 * (i / 3) + k / 3][ 3 * (j / 3) + k % 3] != '.' and board[3 * (i / 3) + k / 3][ 3 * (j / 3) + k % 3] == n:
                return False
        return True
            
            
