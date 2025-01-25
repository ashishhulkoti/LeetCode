# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1=l1
        n2=l2
        sum=0
        carry=0
        while n1.next and n2.next:
            sum=n1.val+n2.val+carry
            n1.val=sum%10
            carry=sum//10
            n1=n1.next
            n2=n2.next
        
        sum=n1.val+n2.val+carry
        n1.val=sum%10
        carry=sum//10

        if n2.next:
            n1.next=n2.next
        
        if carry == 0:
            return l1
        
        curr=n1
        n1=n1.next
        while n1:
            # n1=n1.next
            sum=n1.val+carry
            n1.val=sum%10
            carry=sum//10
            curr=n1
            n1=n1.next
        if carry == 1:
            curr.next=ListNode(1)
        return l1


    