class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for x in range(n)] for y in range(n)] 
        res = []
        diag1 = [1] * (2*n-1) #right diagonal
        diag2 = [1] * (2*n-1) #left diagonal
        cols = [1] * n
        rows = [1] * n
        self.dfs(0,n,res,board,diag1,diag2,rows,cols)
        return res
    
    def dfs(self,y,n,res,board,diag1,diag2,rows,cols):
        # if level out of board
        if y == n:
            #print board
            res.append([''.join(row) for row in board])
            return
        #for each board[level][0 to n]
        for x in range(0,n):
            if self.check(x,y,n,diag1,diag2,rows,cols):
                continue
            #set blocks for row, col, diagonals
            self.setBlocks(x,y,n,board,diag1,diag2,rows,cols)
            self.dfs(y+1,n,res,board,diag1,diag2,rows,cols)
            #remove blocks for row,col, diagonals
            self.removeBlocks(x,y,n,board,diag1,diag2,rows,cols)
            
    def check(self,x,y,n,diag1,diag2,rows,cols):
        return not diag1[x+y] or not diag2[x-y+(n-1)] or not cols[y] or not rows[x]
    
    def setBlocks(self,x,y,n,board,diag1,diag2,rows,cols):
        diag1[x+y] = 0
        diag2[x-y+(n-1)] = 0
        cols[y] = 0
        rows[x] = 0
        board[y][x] = 'Q'

    def removeBlocks(self,x,y,n,board,diag1,diag2,rows,cols):
        diag1[x+y] = 1
        diag2[x-y+(n-1)] = 1
        rows[x] = 1
        cols[y] = 1
        board[y][x] = '.'
        
