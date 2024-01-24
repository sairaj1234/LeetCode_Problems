class Solution:
    def reverse(self, x: int) -> int:
        MIN = -(2 ** 31)       
        MAX = 2 ** 31 - 1 
        if x==0:
            result=0
        elif x>0:
            n=0
            n1=str(x)
            l=list(map(int,n1))
            l=l[::-1]
            l2=int("".join(map(str,l)))
            result=l2
            
        else:
            l=str(x)[1:]
            l=l[::-1]
            l="-"+l
            result=int(l)
        if result<MIN or result>MAX:  
            return 0
        return result
            
            
            
                
                
                
        