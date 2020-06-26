# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.nums = []
        self.search(root.right)
        self.nums.append(root.val)
        self.search(root.left)
        return self.nums[k - 1]

    def search(self, node):
        if node is None:
            return
        self.search(node.right)
        self.nums.append(node.val)
        self.search(node.left)