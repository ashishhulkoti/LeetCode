# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def validHelper(node,parentVal,rootVal,left):
            if not node:
                return True
            if left:
                if node.val >= parentVal or node.val<=rootVal:
                    return False
                if not validHelper(node.left,node.val,rootVal,True) or not validHelper(node.right,node.val,parentVal,False):
                    return False
            else:
                if node.val <= parentVal or node.val>=rootVal:
                    return False
                if not validHelper(node.left,node.val,parentVal,True) or not validHelper(node.right,node.val,rootVal,False):
                    return False
            return True

        
        return validHelper(root.left,root.val,float("-inf"),True) and validHelper(root.right,root.val,float("inf"),False) 

             
            