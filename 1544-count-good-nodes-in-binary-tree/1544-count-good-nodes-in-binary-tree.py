# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfsHelper(node, greatest):
            nonlocal count
            if not node:
                return
            
            currG = max(node.val, greatest)
            dfsHelper(node.left, currG)
            dfsHelper(node.right, currG)
            if node.val>=greatest:
                count+=1
        dfsHelper(root,float("-inf"))
        return count