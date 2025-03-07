# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kthelement=-1
        flag=False
        def khelper(node):
            nonlocal k
            nonlocal kthelement
            nonlocal flag
            if not node:
                return
            
            khelper(node.left)
            k-=1
            if k==0:
                flag=True
                kthelement=node.val
            if flag:
                return
            khelper(node.right)
        khelper(root)
        return kthelement

