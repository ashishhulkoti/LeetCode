# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':



        def lca_helper(node,p,q):    
            if not node:
                return None
            
            if node==p or node==q:
                return node
            
            left = lca_helper(node.left,p,q)
            right = lca_helper(node.right,p,q)
                
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
            return None

        
        return lca_helper(root,p,q)