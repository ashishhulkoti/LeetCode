# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        seen_level=-1
        ans=[]
        
        def view_helper(node,currLevel):
            nonlocal seen_level
            if not node:
                return
            if currLevel>seen_level:
                ans.append(node.val)
                seen_level+=1
                
            view_helper(node.right,currLevel+1)
            view_helper(node.left,currLevel+1)

        view_helper(root,0)
        return ans