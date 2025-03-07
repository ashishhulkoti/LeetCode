# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_que=[]
        right_que=[]
        if root.left:
            left_que.append(root.left)
        if root.right:
            right_que.append(root.right)

        while left_que and right_que:
            ln=left_que.pop(0)
            rn=right_que.pop(0)
            if ln.val != rn.val:
                return False
            if ln.left and rn.right:
                left_que.append(ln.left)
                right_que.append(rn.right)
            elif ln.left or rn.right:
                return False
            if ln.right and rn.left:
                left_que.append(ln.right)
                right_que.append(rn.left)
            elif ln.right or rn.left:
                return False 
        if left_que or right_que:    
            return False
        return True
            