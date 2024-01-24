class Solution:
    def isValid(self, s: str) -> bool:
        s1=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                s1.append(i)
                
            if len(s1)==0:
                return False
            if i==']':
                if s1.pop()!='[':
                    return False
            if i==')':
                if s1.pop()!='(':
                    return False
            if i=='}':
                if s1.pop()!='{':
                    return False
        if len(s1)==0:
            return True
        return False
                
                
        