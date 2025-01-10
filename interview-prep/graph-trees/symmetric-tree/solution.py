# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSymmetricNodes(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None or p.val != q.val:
            return False
        return self.checkSymmetricNodes(p.left, q.right) and self.checkSymmetricNodes(p.right, q.left)
    def isSymmetric(self, root) -> bool:
        if root == None:
            return True
        return self.checkSymmetricNodes(root.left, root.right)
        