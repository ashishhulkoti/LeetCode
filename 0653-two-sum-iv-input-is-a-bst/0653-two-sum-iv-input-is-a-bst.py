# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        compl_dict={}

        def inorderTraverse(node):
            nonlocal compl_dict
            if not node:
                return False
            if (k-node.val) in compl_dict:
                return True
            compl_dict[node.val]=1
            if inorderTraverse(node.left) or inorderTraverse(node.right):
                return True
            return False
        return inorderTraverse(root)
            


