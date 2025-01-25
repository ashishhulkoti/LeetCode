# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def solution_helper(n1,n2,carry):
    num1=0
    num2=0
    if not n1 and not n2:
        if carry != 0:
            return ListNode(1)
        return None
    if n1:
        num1=n1.val
        n1=n1.next
    if n2:
        num2=n2.val
        n2=n2.next
    sum=num1+num2+carry
    node=ListNode((sum)%10)
    node.next=solution_helper(n1,n2,int((sum)/10))
    return node

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return solution_helper(l1,l2,0)
        