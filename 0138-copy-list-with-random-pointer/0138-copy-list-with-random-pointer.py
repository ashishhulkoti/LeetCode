"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        node_dict={}
        headn=Node(head.val)
        node_dict[head]=headn

        # prev=None
        curr=head
        while curr:
            node=None
            if curr.next:
                if curr.next in node_dict:
                    node_dict[curr].next=node_dict[curr.next]
                else:
                    nnode=Node(curr.next.val)
                    node_dict[curr].next=nnode
                    node_dict[curr.next]=nnode
            if curr.random:
                if curr.random in node_dict:
                    node_dict[curr].random=node_dict[curr.random]
                else:
                    nnode=Node(curr.random.val)
                    node_dict[curr].random=nnode
                    node_dict[curr.random]=nnode
            curr=curr.next
        return headn

                
