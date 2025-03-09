# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        noSum=0

        # print([])
        def sumHelper(node,sums):
            nonlocal noSum
            curr_sum=copy.deepcopy(sums)
            if not node:
                return
            if node.val==targetSum:
                noSum+=1
            for i in range(len(curr_sum)):
                curr_sum[i]+=node.val
                if curr_sum[i]==targetSum:
                    noSum+=1
            curr_sum.append(node.val)
            # print(curr_sum)
            sumHelper(node.left,curr_sum)
            sumHelper(node.right,curr_sum)
        sumHelper(root,[])
        return noSum
