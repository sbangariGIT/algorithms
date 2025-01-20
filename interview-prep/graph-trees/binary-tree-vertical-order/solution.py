# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helperVerticalOrder(self, node , i, map_order):
        if node == None:
            return
        if i not in map_order:
            map_order[i] = []
        map_order[i].append(node.val)
        self.helperVerticalOrder(node.left, i - 1, map_order)
        self.helperVerticalOrder(node.right, i + 1, map_order)
    def verticalOrder(self, root):
        if root == None:
            return []
        map_order = {}
        curr = [(root, 0)]
        result = []
        while len(curr) != 0:
            node, index = curr.pop(0)
            if index not in map_order:
                map_order[index] = []
            map_order[index].append(node.val)
            if node.left != None:
                curr.append((node.left, index - 1))
            if node.right != None:
                curr.append((node.right, index + 1))
        keys = list(map_order.keys())
        keys.sort()
        for j in keys:
            result.append(map_order[j])
        return result

        