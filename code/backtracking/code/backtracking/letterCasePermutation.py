class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        tmp = ""
        self.dfs(0,tmp,res,S)
        
        return res
        
    def dfs(self,i,tmp,res,s):
        if i == len(s):
            res.append(tmp)
            return  #out of bound should return
        
        # Suppose to be a for loop, but only 3 iterations
        if s[i].isdigit():   
            self.dfs(i+1,tmp+s[i],res,s)
            return  #if i is digit ignore the letters and go to next level

        self.dfs(i+1,tmp + s[i].lower(),res,s)
        self.dfs(i+1,tmp + s[i].upper(),res,s)
