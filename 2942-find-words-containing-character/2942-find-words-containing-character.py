class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l=[]
        c=0
        for i in words:
          
            if x in i:
                l.append(c)
            c+=1
        return l