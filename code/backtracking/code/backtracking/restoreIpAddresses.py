class Solution(object):
    def restoreIpAddressesGeneral(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        tmp = ""
        res = []
        
        self.dfs(s,0,tmp,res,0)
        
        return res
        
    def dfs(self,s,l,tmp,res,count):
        if count > 4:
            return
        
        if len(s) == l and count == 4: #用光所有string
            res.append(tmp[1:])
            return
        
        for i in range(l,len(s)):
            if i + 1 > len(s):
                return
            subS = s[l:i+1] #subString 分割

            if (subS[0] == '0' and len(subS) > 1) or ( len(subS) >= 3 and int(subS) >= 256): #不符合條件，找同層下一個
                continue
            self.dfs(s,i+1,tmp+'.'+subS,res,count+1) #到下一層


    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        tmp = ""
        res = []
        
        self.dfs(s,0,tmp,res,0)
        
        return res
        
    def dfs(self,s,index,tmp,res,count):
        if count > 4:
            return
        
        if len(s) == index and count == 4: #用光所有string
            res.append(tmp[1:])
            return
        
        for i in range(1,4):
            if index + i > len(s):
                return
            subS = s[index:index+i] #subString 分割

            if (subS[0] == '0' and len(subS) > 1) or (i == 3 and int(subS) >= 256): #不符合條件，找同層下一個
                continue
            self.dfs(s,index+i,tmp+'.'+subS,res,count+1) #到下一層
        
