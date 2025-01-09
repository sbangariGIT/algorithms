# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root != None:
            if root.val == p.val or root.val == q.val:
                return root
            if root.val > p.val and root.val > q.val:
                root = root.left
                continue
            if root.val < p.val and root.val < q.val:
                root = root.right
                continue
            return root
        