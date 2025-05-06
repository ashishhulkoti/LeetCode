# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=None
        counter=0
        def dfsHelper(node):
            nonlocal ans,k,counter
            if not node :
                return False
            if dfsHelper(node.left):
                return True
            counter+=1
            if counter == k:
                ans=node.val
                return True
            if dfsHelper(node.right):
                return True
        dfsHelper(root)
        return ans
