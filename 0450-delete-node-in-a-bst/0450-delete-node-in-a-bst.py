# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def moveSubTree(node, subRoot):
            if not node.left:
                node.left = subRoot
                return

            moveSubTree(node.left, subRoot)

        def searchNode(node):
            if not node:
                return None, False
            
            if node.val == key:
                if not node.left:
                    return node.right, True
                if not node.right:
                    return node.left, True
                
                moveSubTree(node.right,node.left)
                return node.right,True
            
            subNode, flag = searchNode(node.left)
            if flag:
                node.left = subNode
                return None, False
            subNode, flag = searchNode(node.right)
            if flag:
                node.right = subNode
            return None, False
        
        node, flag = searchNode(root)
        if flag:
            return node
        return root