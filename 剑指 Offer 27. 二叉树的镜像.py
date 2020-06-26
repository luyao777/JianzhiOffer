# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.left != None:
            self.mirrorTree(root.left)
        if root.right != None:
            self.mirrorTree(root.right)
        root.right, root.left = root.left, root.right
        return root
