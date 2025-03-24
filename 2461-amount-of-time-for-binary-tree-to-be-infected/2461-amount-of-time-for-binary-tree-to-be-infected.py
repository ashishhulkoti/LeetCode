# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        topPath=0
        bottomPath=0

        def treeTraversal(node) -> int:
            nonlocal topPath
            nonlocal bottomPath
            if not node:
                return 0
            
            if node.val==start:
                bottomPath = max(treeTraversal(node.left),treeTraversal(node.right))
                return -1
            
            left = treeTraversal(node.left)
            right = treeTraversal(node.right)
            if right < 0:
                if right*(-1)+left > topPath:
                    topPath=right*(-1)+left
                return right-1
            elif left < 0:
                if left*(-1)+right > topPath:
                    topPath=left*(-1)+right
                return left-1
            return 1 + max(left,right)

        treeTraversal(root)
        return max(topPath,bottomPath)
            
