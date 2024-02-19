class Solution:
    def reverseWords(self, s: str) -> str:
        s1=''
        s=s.split()[::-1]
        for i in range(len(s)-1):
            s1=s1+s[i]
            s1=s1+' '
        s1=s1+s[-1]
        return s1
            