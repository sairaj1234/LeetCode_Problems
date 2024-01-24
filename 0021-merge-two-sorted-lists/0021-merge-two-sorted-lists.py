# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur=temp=temp1=ListNode()
        if l1==None:
            return l2
        elif l2==None:
            return l1
        while (l1!=None) and (l2!=None):
            temp2=ListNode()
            if l1.val<=l2.val:
                cur=l1
                temp2.val=cur.val
                l1=l1.next
            else:
                cur=l2
                temp2.val=cur.val
                l2=l2.next
            temp.next=temp2
            temp=temp.next
        temp.next=l1 or l2
        return temp1.next







        


        