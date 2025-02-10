# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr=head.next
        prev=head
        prev_val=prev.val
        while curr:
            if curr.val==prev_val:
                prev_val=curr.val
            else:
                prev.next=curr
                prev=curr
                prev_val=prev.val
            curr=curr.next
        prev.next=curr
        return head