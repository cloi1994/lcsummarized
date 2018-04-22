class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        n = len(board)
        
        m = len(board[0])
        
        visited = [[0 for _ in range(m)] for i in range(n)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check(0,i,j,word,visited,board):
                    return True
        return False
    
    def check(self,index,i,j,word,visited,board):
        if index == len(word):
            return True
        
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or visited[i][j]:
            return False
        if word[index] != board[i][j]:
            return False
        
        visited[i][j] = 1
        
        exist = self.check(index+1,i+1,j,word,visited,board) or self.check(index+1,i,j+1,word,visited,board) or self.check(index+1,i-1,j,word,visited,board) or self.check(index+1,i,j-1,word,visited,board)
        
        visited[i][j] = 0
        
        return exist
        
