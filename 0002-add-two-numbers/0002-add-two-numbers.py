# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l=ListNode()
        head=l
        s1=''
        s2=''
        
        temp=l1
        temp2=l2
        while(temp!=None):
            s1=s1+str(temp.val)
            temp=temp.next
        while(temp2!=None):
            s2=s2+str(temp2.val)
            temp2=temp2.next
        n1=int(s1[::-1])
        n2=int(s2[::-1])
        n3=n1+n2
        s3=str(n3)[::-1]
        for i in s3:
            l.next=ListNode(i)
            l=l.next
        return head.next
        
        
        