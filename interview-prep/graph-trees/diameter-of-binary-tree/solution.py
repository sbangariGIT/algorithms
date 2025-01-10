# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.high = 0
    def height(self, root):
        if root == None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        current_diameter = left + right
        self.high = max(self.high, current_diameter)
        return 1 + max(left, right)
    def diameterOfBinaryTree(self, root) -> int:
        self.height(root)
        return self.high

        