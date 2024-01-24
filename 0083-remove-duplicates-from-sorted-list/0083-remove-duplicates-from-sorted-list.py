# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=cur=head
        if head==None:
            return head
        cur=cur.next
        
        while(cur!=None):
            
            if pre.val==cur.val:
                pre.next=cur.next
                cur=pre.next
            else:
                cur=cur.next
                pre=pre.next
        return head
