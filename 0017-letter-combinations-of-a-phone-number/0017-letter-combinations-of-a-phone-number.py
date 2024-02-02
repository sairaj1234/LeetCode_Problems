class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l=[]
        l2=[]
        h={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if len(digits)==0:
            return l
        if len(digits)==1:
            for i in h[digits]:
                l.append(i)
            return l
        l=[""]
        for i in digits:
            
            tmp=[]
            for c in h[i]:
                for o in l:
                    tmp.append(o+c)
            l=tmp
        return l
                    
                
            
        
            
            
        
                