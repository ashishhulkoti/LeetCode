# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        currQue=[]
        nextQue=[]
        if not root:
            return []
        currQue.append(root)
        ltor=True
        ans=[]
        while True:
            curr_ans=[]
            while currQue:
                if ltor:
                    node=currQue.pop(0)
                    curr_ans.append(node.val)
                    if node.left:
                        nextQue.append(node.left)
                    if node.right:
                        nextQue.append(node.right)
                else:
                    node=currQue.pop()
                    curr_ans.append(node.val)
                    if node.right:
                        nextQue.insert(0,node.right)
                    if node.left:
                        nextQue.insert(0,node.left)
            ans.append(curr_ans)
            currQue=nextQue
            nextQue=[]
            ltor = not ltor
            if not currQue:
                return ans
            