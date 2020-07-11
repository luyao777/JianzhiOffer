# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode,
                             q: TreeNode) -> TreeNode:
        if not root:
            return False
        if root == p or root == q:
            return root
        right_state = self.lowestCommonAncestor(root.right, p, q)
        left_state = self.lowestCommonAncestor(root.left, p, q)

        if right_state and left_state:
            return root

        return right_state or left_state
