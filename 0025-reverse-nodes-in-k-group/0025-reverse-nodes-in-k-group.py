# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def reverseSubList(self, startNode, endNode):
        prevNode = None
        currNode = startNode
        nextNode = None
        while currNode != endNode:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        currNode.next = prevNode

    def reverseHelper(self, headNode, k):
        tailNode = None
        currNode = headNode
        i = 1
        prevNode = None
        while i <= k:
            if not currNode:
                return headNode
            prevNode = currNode
            currNode = currNode.next
            i+=1
        if i-1 != k:
            return headNode
        nextHead = self.reverseHelper(currNode, k)
        self.reverseSubList(headNode, prevNode)
        
        headNode.next = nextHead

        return prevNode

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return self.reverseHelper(head, k)