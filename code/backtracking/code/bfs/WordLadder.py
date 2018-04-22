class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        step = 0
        l = len(beginWord)
        q = [beginWord]
        
        if endWord not in wordList:
            return 0
        
        while len(q) != 0:
            step += 1
            for _ in range(len(q)):
                w = q.pop(0)
                #change the base word from a - z for each character in that word
                for i in range(l):
                    ch = w[i]
                    for letter in 'abcdefghijklmnopqrstuvwxyz':
                        w = w[:i] + letter + w[i + 1:]
                        if w == endWord:
                            return step + 1
                        if w not in wordList:
                            continue
                        #find word that is in wordlist
                        q.append(w)
                        wordList.remove(w) 
                    #restore
                    w = w[:i] + ch + w[i + 1:]   
        return 0
