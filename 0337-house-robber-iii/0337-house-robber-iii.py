# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def robHelper(node, rob):
            if not node:
                return 0
            
            if rob:
                return node.val + robHelper(node.left,False) + robHelper(node.right,False)
            else:
                return max(max(robHelper(node.left,False) + robHelper(node.right,False), robHelper(node.left,True) + robHelper(node.right, True)), max(robHelper(node.left,True) + robHelper(node.right,False), robHelper(node.left,False) + robHelper(node.right, True)))
        
        return max(robHelper(root, True), robHelper(root, False))