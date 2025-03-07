# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def diameter_helper(node):
            nonlocal diameter
            if not node:
                return 0
            left=diameter_helper(node.left)
            right=diameter_helper(node.right)
            sum_curr = left + right + 1
            if sum_curr > diameter:
                diameter = sum_curr
            
            return max(left,right)+1
        diameter_helper(root)
        return diameter - 1 