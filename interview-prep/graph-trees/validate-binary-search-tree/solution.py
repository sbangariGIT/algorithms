# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getArray(self, root, current):
        if root == None:
            return
        self.getArray(root.left, current)
        current.append(root.val)
        self.getArray(root.right, current)

    def isValidBST(self, root) -> bool:
        current = []
        self.getArray(root, current)
        for i in range(len(current)-1):
            if current[i] >= current[i+1]:
                return False
        return True