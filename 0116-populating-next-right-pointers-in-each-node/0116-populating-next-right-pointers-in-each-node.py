"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        curr_que=[root]
        next_que=[]
        if not root:
            return root
        curr_que.append(None)
        while True:
            while len(curr_que)>1:
                node=curr_que.pop(0)
                node.next=curr_que[0]
                if node.left:
                    next_que.append(node.left)
                if node.right:
                    next_que.append(node.right)

            if not next_que:
                break
            curr_que=next_que
            next_que=[]
            curr_que.append(None)
        return root