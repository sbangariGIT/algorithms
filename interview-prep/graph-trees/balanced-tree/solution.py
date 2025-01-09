# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root):
        if root == None:
            return 0, True
        right, balancedr = self.getHeight(root.right)
        left, balancedl = self.getHeight(root.left)
        balanced = True
        if abs(left-right) > 1:
            balanced = False
        if not balancedl or not balancedr:
            balanced = False
        return max(right, left) + 1, balanced

    def isBalanced(self, root) -> bool:
        if root == None:
            return True
        right, balancedr = self.getHeight(root.right)
        left, balancedl = self.getHeight(root.left)

        if not balancedl or not balancedr:
            return False 
        if abs(left-right) > 1:
            return False
        return True