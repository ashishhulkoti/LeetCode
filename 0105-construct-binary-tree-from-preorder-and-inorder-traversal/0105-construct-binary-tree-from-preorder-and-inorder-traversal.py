# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def buildTree(left,right):
            nonlocal preorder_ind
            if left>right:
                return None
            
            root_value=preorder[preorder_ind]
            root=TreeNode(root_value)

            preorder_ind+=1

            root.left=buildTree(left,inorder_map[root_value]-1)
            root.right=buildTree(inorder_map[root_value]+1,right)
            return root
        preorder_ind=0
        inorder_map={}
        for index,value in enumerate(inorder):
            inorder_map[value]=index
        
        return buildTree(0,len(preorder)-1)