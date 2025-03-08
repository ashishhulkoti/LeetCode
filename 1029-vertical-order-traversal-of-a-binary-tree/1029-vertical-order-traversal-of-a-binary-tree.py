# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        n_dict=defaultdict(lambda: defaultdict(list))
        # n_dict=defaultdict(defaultdict(list))
        def traversalHelper(node,col,row):
            nonlocal n_dict
            if not node:
                return
            n_dict[col][row].append(node.val)
            traversalHelper(node.left,col-1,row+1)
            traversalHelper(node.right,col+1,row+1)
        traversalHelper(root,0,0)
        ans=[]
        for col in sorted(n_dict.keys()):
            tmp=[]
            for row in sorted(n_dict[col].keys()):
                tmp.extend(sorted(n_dict[col][row]))
            ans.append(tmp)
        return ans

