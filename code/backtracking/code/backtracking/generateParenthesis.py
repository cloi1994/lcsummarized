class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        
        self.dfs(0,0,[],res,n)
        
        return res
        
    def dfs(self,left,right,tmp,res,n):
        
        if left == n and right == n:
            res.append(''.join(tmp))
            return #reach to boundard
        
        #act as for loop
        if left < n:
            tmp.append('(')
            self.dfs(left+1,right,tmp,res,n)
            tmp.pop()
        if right < left:
            tmp.append(')')
            self.dfs(left,right+1,tmp,res,n)
            tmp.pop()
        
    # Time : O(n!)
    # Space : O(2n)
