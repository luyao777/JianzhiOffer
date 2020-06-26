# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        cur_level = []
        next_level = []

        if root == None:
            return result

        result.append([root.val])
        if root.left is not None:
            cur_level.append(root.left)
        if root.right is not None:
            cur_level.append(root.right)

        while (cur_level != []):
            res = []
            while (cur_level != []):
                cur_node = cur_level.pop(0)
                res.append(cur_node.val)
                if cur_node.left is not None:
                    next_level.append(cur_node.left)
                if cur_node.right is not None:
                    next_level.append(cur_node.right)
            result.append(res)
            cur_level = next_level
            next_level = []
        return result
