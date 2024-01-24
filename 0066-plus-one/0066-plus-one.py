class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=0
        s=''
        l=[]
        for i in digits:
            s+=str(i)
        k=int(s)+1
        s1=str(k)
        for i in s1:
            l.append(int(i))
        return l

        