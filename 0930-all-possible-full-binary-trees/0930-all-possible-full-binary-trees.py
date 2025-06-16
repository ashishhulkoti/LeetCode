# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def buildTree(num):
            if num ==0:
                return [TreeNode(0)]
            if num == 2:
                currNode = TreeNode(val = 0, left = TreeNode(0), right = TreeNode(0))
                return [currNode]
            
            avlNodes = num - 2
            toLeftChild = 0
            nodesVar = []
            while toLeftChild <= avlNodes:
                leftVar, rightVar = buildTree(toLeftChild), buildTree(avlNodes - toLeftChild)
                for leftNode in leftVar:
                    for rightNode in rightVar:
                       nodesVar.append(TreeNode(0,leftNode,rightNode))
                toLeftChild+=2
            return nodesVar
        return buildTree(n-1)