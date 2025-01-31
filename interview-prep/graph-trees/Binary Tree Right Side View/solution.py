# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_max = 0
    
    def helper(self, root, book, level):
        if root == None:
            return
        if level not in book:
            book[level] = []
        book[level].append(root.val)
        self.max_max = max(self.max_max, level)
        self.helper(root.left, book, level + 1)
        self.helper(root.right, book, level + 1)

    def rightSideView(self, root):
        book = {}
        result = []
        self.helper(root, book, 0)
        if len(book) > 0:
            for i in range(0, self.max_max + 1):
                result.append(book[i][-1])
        return result
