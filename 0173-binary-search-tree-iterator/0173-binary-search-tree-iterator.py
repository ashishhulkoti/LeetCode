# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.treeArray = []
        self.pointer = -1
        def inorderTraverse(node):
            if not node:
                return
            inorderTraverse(node.left)
            self.treeArray.append(node.val)
            inorderTraverse(node.right)
        inorderTraverse(root)


    def next(self) -> int:
        self.pointer+=1
        return self.treeArray[self.pointer]

    def hasNext(self) -> bool:
        return True if self.pointer+1 < len(self.treeArray) else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()