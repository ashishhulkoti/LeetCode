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
        node_dict = {}
        node_dict[None] = None
        def dfs(node):
            if not node:
                return None
            
            if node not in node_dict:
                node_dict[node] = Node(node.val)
            
            node_dict[node].next = dfs(node.next)
            node_dict[node].random = node_dict[node.random]

            return node_dict[node]
        
        return dfs(head)
