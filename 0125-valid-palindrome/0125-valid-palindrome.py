class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l='abcdefghijklmnopqrstuvwxyz1234567890'
        k=''
        for i in s:
            if i in l:
                k+=i
        k1=k[::-1]
        if k1==k:
            return True
        else:
            return False
        
                
        