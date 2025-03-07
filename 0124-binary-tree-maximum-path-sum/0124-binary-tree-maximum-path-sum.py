# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum=float("-inf")
        def sum_helper(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left=sum_helper(node.left)
            right=sum_helper(node.right)
            sum_root=right+left+node.val
            if sum_root > max_sum:
                max_sum=sum_root
            
            if node.val>max_sum:
                max_sum=node.val
            
            if right+node.val>max_sum:
                max_sum=right+node.val
            
            if left+node.val>max_sum:
                max_sum=left+node.val

            return max(node.val,max(right+node.val,left+node.val))

        root_sum=sum_helper(root)
        return max(max_sum,root_sum)
