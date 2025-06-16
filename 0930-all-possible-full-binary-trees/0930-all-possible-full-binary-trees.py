# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo = {}
        def buildTree(num):
            if num in memo:
                return memo[num]
            if num ==0:
                memo[num] = [TreeNode(0)]
                return memo[num]
            if num == 2:
                currNode = TreeNode(val = 0, left = TreeNode(0), right = TreeNode(0))
                memo[num] = [currNode]
                return memo[num]
            
            avlNodes = num - 2
            toLeftChild = 0
            nodesVar = []
            while toLeftChild <= avlNodes:
                leftVar, rightVar = buildTree(toLeftChild), buildTree(avlNodes - toLeftChild)
                for leftNode in leftVar:
                    for rightNode in rightVar:
                       nodesVar.append(TreeNode(0,leftNode,rightNode))
                toLeftChild+=2
            memo[num] = nodesVar
            return memo[num]
        return buildTree(n-1)